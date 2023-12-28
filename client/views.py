from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from django.contrib import messages
from django.contrib.auth import logout
from .forms import ClientForm, RetraitCreditForm
from .models import Client, TotalCredit, RetraitCredit
from .utils import demande_credit

# Create your views here.

def connexion(request):
 if request.method == 'POST':
  form = ClientForm(request.POST)
  get_number = request.POST.get('numero')
  try:
    client =  Client.objects.get(numero=get_number)
    if client is None:
      print('erreur')
    request.session['client_id'] = client.id
    return redirect('client', client_id=client.id)
       
  except Client.DoesNotExist:
    return render(request, 'client/connexion.html', {'form': form})
    
 return render(request, 'client/connexion.html', {'form': ClientForm()})

#def client_user_check(user):
  #return 'client_id' in user.session

#@login_required(login_url='connexion')
#@user_passes_test(client_user_check)
def client(request, client_id):
  client_id = get_object_or_404(Client, id=client_id)
  total_credit = TotalCredit.objects.filter(client=client_id).first()
  return render(request, 'client/client.html', {'client': client_id, 'total_credit': total_credit})

def deconnexion(request):
  logout(request)
  return redirect('connexion');

def retrait(request, client_id):
  client = get_object_or_404(Client, id=client_id)
  credit = TotalCredit.objects.filter(client=client).first()
  if request.method == 'POST':
    form = RetraitCreditForm(request.POST or None)
    if form.is_valid():
      get_quantite = form.cleaned_data.get('quantite')
      get_data = form.cleaned_data.get('data_forfait')
      get_data_mo = form.cleaned_data.get('data_mo')
      if get_quantite >= 50 and get_quantite <= credit.total_credit:
        try:
          with transaction.atomic():
            credit.total_credit -= get_quantite
            credit.save()
            retrait_credit = RetraitCredit(
              total_credit=credit, 
              quantite=get_quantite, 
              data_forfait=get_data, 
              data_mo=get_data_mo
            )
            retrait_credit.save()
            sms_message = f"Le client {client.numero} a effectué une conversion de {get_quantite} crédits pour {get_data} Mo. Message de Application KOMO1"
            demande_credit(sms_message)
          return redirect('client', client_id=client_id)
        except Exception as e:
          print(f"Erreur: {e}")
          return HttpResponse('Erreur lors de la transaction !')
          
      elif get_quantite > 0 and get_quantite < 50:
        messages.error(request, 'La convertion se fait à 50 crédits.')
        return render(request, 'client/retraitcredit.html', {'form': form, 'client': client, 'credit': credit, 'titre': 'Retrait de crédits', })

      elif get_quantite == 0:
        messages.error(request, "Entrer une valeur superieur à 0")
        return render(request, 'client/retraitcredit.html', {'form': form, 'client': client, 'credit': credit, 'titre': 'Retrait de crédits', })
        
      elif get_quantite > credit.total_credit:
        messages.error(request, "Vous n'avez pas cette quantité de crédits.")
        return render(request, 'client/retraitcredit.html', {'form': form, 'client': client, 'credit': credit, 'titre': 'Retrait de crédits', })

  
  else:
    form = RetraitCreditForm()
        
  return render(request, 'client/retraitcredit.html', {'form': form, 'client': client, 'credit': credit, 'titre': 'Retrait de crédits'})

def forfait(request, client_id):
  client = get_object_or_404(Client, id=client_id)
  context = {
    'client': client,
    'titre': 'Forfait Komo1'
  }
  return render(request, 'client/forfaitkomo.html', context=context)

def historique(request, client_id):
  client = get_object_or_404(Client, id=client_id)
  retrait = RetraitCredit.objects.filter(total_credit__client=client)
  context = {
    'client': client,
    'retrait': retrait,
    'titre': 'Historique'
  }
  return render(request, 'client/historique.html', context=context)
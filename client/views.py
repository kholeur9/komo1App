from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from django.contrib import messages
from django.contrib.auth import logout
from datetime import datetime
from django.contrib import messages
from .forms import ClientForm, RetraitCreditForm
from .models import Client, TotalCredit, RetraitCredit
#from .utils import demande_credit
from .message import demande_credit

# Create your views here.
def connexion(request):
  
  if request.method == 'POST':
      form = ClientForm(request.POST)
      get_number = request.POST.get('numero')
      try:
        client = Client.objects.get(numero=get_number)
        if client:
          request.session['client_id'] = client.id
          print("Session", request.session['client_id'])
          return redirect('client', client_id=client.id)
      except Client.DoesNotExist:
        messages.error(request, 'Numéro de client inconnu')
        
  else:
    form = ClientForm()

  return render(request, 'client/connexion.html', {'form': ClientForm()})

def client(request, client_id):
    client_id = get_object_or_404(Client, id=client_id)
    total_credit = TotalCredit.objects.filter(client=client_id).first()
    context = {
      'client': client_id, 
      'total_credit': total_credit,
      'titre' : 'Accueil',
    }
    return render(request, 'client/client.html', context=context)

def deconnexion(request):
  logout(request)
  return redirect('connexion')

def retrait(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    credit = TotalCredit.objects.filter(client=client).first()
    retraits = RetraitCredit.objects.filter(total_credit__client=client).order_by('-date')

    if request.method == 'POST':
      form = RetraitCreditForm(request.POST or None)
      if form.is_valid():
        get_quantite = form.cleaned_data.get('quantite')
        get_data = form.cleaned_data.get('data_forfait')
        get_last_date = retraits.first().date.date() if retraits.exists() else None
        if (get_quantite >= 50 and get_quantite <= credit.total_credit 
            and (get_last_date is None or get_last_date != datetime.now().date())):
          try:
            with transaction.atomic():
              credit.total_credit -= get_quantite
              credit.save()
              retrait_credit = RetraitCredit(total_credit=credit,quantite=get_quantite,data_forfait=get_data)
              retrait_credit.save()
              
              sms_message = f"Le client {client.numero} a effectué une conversion de {get_quantite} crédits pour un forfait de {get_data} Mo. De komo1App.";
              demande_credit(sms_message)
              retrait_credit.status = 'Approuvé'
            return redirect('client', client_id=client_id)
          except Exception as e:
            print(f"Erreur: {e}")
            return HttpResponse('Erreur lors de la transaction !')

        elif get_last_date is not None and get_last_date == datetime.now().date():
          messages.error(request, "Vous avez droit à un retrait par jour.")
        elif get_quantite > credit.total_credit:
          messages.error(request, f"Vous n'avez pas {get_quantite} crédits.")
    else:
        form = RetraitCreditForm()
    context = {
        'client': client,
        'credit': credit,
        'form': form,
        'titre': 'Retrait de crédit',
    }
    return render(
        request, 'client/retraitcredit.html', context)


def forfait(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    context = {'client': client, 'titre': 'Forfait Komo1'}
    return render(request, 'client/forfaitkomo.html', context=context)


def historique(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    retrait = RetraitCredit.objects.filter(total_credit__client=client)
    context = {'client': client, 'retrait': retrait, 'titre': 'Historique'}
    return render(request, 'client/historique.html', context=context)


def service_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)

    context = {'client': client, 'titre': 'Service Client'}
    return render(request, 'client/client_service.html', context=context)

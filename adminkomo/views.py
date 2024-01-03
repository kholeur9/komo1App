from django.shortcuts import render, redirect
from .forms import AdminKomoForm, ExcelForm
from .models import ExcelFile
from client.models import Client, Forfait, TotalGeneral
from .utils.excel import send_data
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages, auth


# Create your views here.

def connexion(request):
  if request.method == 'POST':
    form = AdminKomoForm(request.POST)
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request, user)
      return redirect('adminkomo')
    else:
      messages.error(request, 'Identifiants incorrects')

  else:
    form = AdminKomoForm()
  return render(request, 'adminkomo/connexion.html', {'form': form})

def deconnexion(request):
  auth.logout(request)
  return redirect('connexion')

@login_required(login_url='connexion')
def index(request):
  
  client_count = Client.objects.count()
  forfait_count = Forfait.objects.count()
  total_general = TotalGeneral.objects.first()
  
  p_index = True
  
  context = {
    'clients': client_count,
    'forfaits': forfait_count,
    'total_general': total_general,
    'p_index': p_index,
  }
  return render(request, 'adminkomo/index.html', context=context)

@login_required(login_url='connexion')
def data_excel(request):
 if request.method == 'POST':
  form = ExcelForm(request.POST, request.FILES)
  if form.is_valid():
   data = form.save()
   send_data(data.file.path)
   return render(request, 'adminkomo/excel.html', {'form': form})

 else:
  form = ExcelForm()

 count = ExcelFile.objects.filter(file__endswith = '.xlsx').count()
 all_file = ExcelFile.objects.all()
 p_index = True
 
 context = {
    'form': form,
    'count_field': count,
    'all': all_file,
    'p_index': p_index,
 }
  
 return render(request, 'adminkomo/excel.html', context=context)

@login_required(login_url='connexion')
def demande(request):
  p_index = True

  context = {
    'p_index': p_index,
  }
  return render(request, 'adminkomo/demande.html', context=context)
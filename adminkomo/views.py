from django.shortcuts import render
from .forms import ExcelForm
from .models import Excel
from client.models import Client, Forfait, TotalGeneral
from .utils.excel import send_data
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  
  client_count = Client.objects.count()
  forfait_count = Forfait.objects.count()
  total_general = TotalGeneral.objects.first()
  
  context = {
    'clients': client_count,
    'forfaits': forfait_count,
    'total_general': total_general
  }
  return render(request, 'adminkomo/index.html', context=context)

def data_excel(request):
 if request.method == 'POST':
  form = ExcelForm(request.POST, request.FILES)
  if form.is_valid():
   data = form.save()
   send_data(data.file.path)
   return render(request, 'adminkomo/excel.html', {'form': form})

 else:
  form = ExcelForm()

 count = Excel.objects.filter(file__endswith = '.xlsx').count()
 all_file = Excel.objects.all()
 
 context = {
    'form': form,
    'count_field': count,
    'all': all_file
 }
  
 return render(request, 'adminkomo/excel.html', context=context)

def demande(request):
  return render(request, 'adminkomo/demande.html')
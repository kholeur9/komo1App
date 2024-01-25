from django import forms
from .models import User, ExcelFile
from django.core.exceptions import ValidationError

class AdminKomoForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'password']
    widgets = {
      'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username', 'placeholder': "Nom d'utilisateur"}),
      'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password', 'placeholder' : "Mot de passe"}),
  }

  def __init__(self, *args, **kwargs):
    super(AdminKomoForm, self).__init__(*args, **kwargs)
    self.fields['username'].label = ""
    self.fields['password'].label = ""


class ExcelForm(forms.ModelForm):
 class Meta:
  model = ExcelFile
  fields = ('file',)
  widgets = {
    'file': forms.FileInput(attrs={'type': 'file', 'class': 'input-file', 'id': 'excel'}),
  }

  def clean_file(self):
    uploaded_file = self.cleaned_data.getraw('file')
    existing_file = ExcelFile.objects.filter(file__iexact=uploaded_file.name).first()

    if existing_file:
      return ValidationError("Ce fichier existe déjà")
  
 def __init__(self, *args, **kwargs):
   super().__init__(*args, **kwargs)
   self.fields['file'].label = ''
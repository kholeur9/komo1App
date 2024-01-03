from django import forms
from .models import User, ExcelFile

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
  
 def __init__(self, *args, **kwargs):
   super().__init__(*args, **kwargs)
   self.fields['file'].label = ''
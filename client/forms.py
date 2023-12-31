from django import forms
from .models import Client, RetraitCredit

class ClientForm(forms.ModelForm):
 class Meta:
  model = Client
  fields = ['numero']
  widgets = {
   'numero': forms.TextInput(attrs={'class': 'input', 'id': 'numero'}),
  }

 def __init__(self, *args, **kwargs):
   super(ClientForm, self).__init__(*args, **kwargs)
   #self.instance = None
   self.fields['numero'].label = ''

class RetraitCreditForm(forms.ModelForm):
  class Meta:
    model = RetraitCredit
    fields = ['quantite', 'data_forfait']
    widgets = {
      'quantite': forms.Select(attrs={'class': 'input', 'id': 'quantite'}),
      'data_forfait': forms.NumberInput(attrs={'class': 'input', 'id': 'data_forfait', 'readonly': 'readonly'}),
    }

  def __init__(self, *args, **kwargs):
    super(RetraitCreditForm, self).__init__(*args, **kwargs)
    self.fields['quantite'].label = ''
    self.fields['data_forfait'].label = ''
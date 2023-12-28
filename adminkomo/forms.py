from django import forms
from .models import Excel


class ExcelForm(forms.ModelForm):
 class Meta:
  model = Excel
  fields = ('file',)
  widgets = {
    'file': forms.FileInput(attrs={'type': 'file', 'class': 'input-file', 'id': 'excel'}),
  }
  
 def __init__(self, *args, **kwargs):
   super().__init__(*args, **kwargs)
   self.fields['file'].label = ''
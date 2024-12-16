from django import forms
from .models import Filial

class FilialForm(forms.ModelForm):
    class Meta:
        model = Filial
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }


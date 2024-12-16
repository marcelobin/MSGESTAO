from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'data_nascimento', 'nome_mae', 'telefone', 'email']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }
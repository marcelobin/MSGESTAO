from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'cpf', 'data_nascimento', 'funcao', 'filial', 'celular', 'email']

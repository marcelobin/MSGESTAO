from django import forms
from django.forms import inlineformset_factory
from .models import Loja, Socio, Vendedor

class LojaForm(forms.ModelForm):
    class Meta:
        model = Loja
        fields = [
            'cnpj', 'razao_social', 'nome_fantasia', 'data_constituicao', 'cep', 
            'endereco', 'nro', 'complemento', 'bairro', 'cidade', 'uf', 'telefone', 
            'email', 'filial', 'contato_comercial'
        ]

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['nome', 'cpf', 'data_nascimento', 'celular', 'email']

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nome', 'cpf', 'chave_pix']

# Inline formsets
SocioFormSet = inlineformset_factory(
    parent_model=Loja,
    model=Socio,
    form=SocioForm,
    extra=3,        # quantos campos extras para novos sócios
    can_delete=True
)

VendedorFormSet = inlineformset_factory(
    parent_model=Loja,
    model=Vendedor,
    form=VendedorForm,
    extra=3,
    can_delete=True
)

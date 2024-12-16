from django import forms
from .models import Proposta, Veiculo

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['marca', 'modelo', 'placa', 'renavam', 'chassi', 'valor_veiculo']

class PropostaForm(forms.ModelForm):
    class Meta:
        model = Proposta
        fields = [
            'nro_proposta', 'financeira', 'loja', 'contato_comercial',
            'valor_financiado', 'prazo', 'vendedor'
        ]

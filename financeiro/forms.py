from django import forms
from .models import LancamentoFinanceiro

class LancamentoFinanceiroForm(forms.ModelForm):
    class Meta:
        model = LancamentoFinanceiro
        fields = ['filial', 'data', 'tipo', 'descricao', 'valor']


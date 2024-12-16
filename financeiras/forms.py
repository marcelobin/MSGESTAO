from django import forms
from .models import Financeira

class FinanceiraForm(forms.ModelForm):
    class Meta:
        model = Financeira
        fields = ['nome']

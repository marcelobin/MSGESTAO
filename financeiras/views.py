from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Financeira
from .forms import FinanceiraForm  # Crie um ModelForm simples para Financeira

class ListaFinanceirasView(ListView):
    model = Financeira
    template_name = 'financeiras/lista_financeiras.html'

class CriaFinanceiraView(CreateView):
    model = Financeira
    form_class = FinanceiraForm
    template_name = 'financeiras/criar_financeira.html'
    success_url = reverse_lazy('financeiras:lista')

class EditaFinanceiraView(UpdateView):
    model = Financeira
    form_class = FinanceiraForm
    template_name = 'financeiras/editar_financeira.html'
    success_url = reverse_lazy('financeiras:lista')

class DetalheFinanceiraView(DetailView):
    model = Financeira
    template_name = 'financeiras/detalhe_financeira.html'

class ExcluiFinanceiraView(DeleteView):
    model = Financeira
    template_name = 'financeiras/confirmar_exclusao_financeira.html'
    success_url = reverse_lazy('financeiras:lista')

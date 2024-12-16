from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import LancamentoFinanceiro
from .forms import LancamentoFinanceiroForm  # Crie um form para LançamentoFinanceiro

class ListaLancamentosView(ListView):
    model = LancamentoFinanceiro
    template_name = 'financeiro/lista_lancamentos.html'

class CriaLancamentoView(CreateView):
    model = LancamentoFinanceiro
    form_class = LancamentoFinanceiroForm
    template_name = 'financeiro/criar_lancamento.html'
    success_url = reverse_lazy('financeiro:lista')

class EditaLancamentoView(UpdateView):
    model = LancamentoFinanceiro
    form_class = LancamentoFinanceiroForm
    template_name = 'financeiro/editar_lancamento.html'
    success_url = reverse_lazy('financeiro:lista')

class DetalheLancamentoView(DetailView):
    model = LancamentoFinanceiro
    template_name = 'financeiro/detalhe_lancamento.html'

class ExcluiLancamentoView(DeleteView):
    model = LancamentoFinanceiro
    template_name = 'financeiro/confirmar_exclusao_lancamento.html'
    success_url = reverse_lazy('financeiro:lista')

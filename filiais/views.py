from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Filial
from .forms import FilialForm  # Supondo que você tenha criado um FilialForm

class ListaFiliaisView(ListView):
    model = Filial
    template_name = 'filiais/lista_filiais.html'

class CriaFilialView(CreateView):
    model = Filial
    form_class = FilialForm
    template_name = 'filiais/criar_filial.html'
    success_url = reverse_lazy('filiais:lista')

class EditaFilialView(UpdateView):
    model = Filial
    form_class = FilialForm
    template_name = 'filiais/editar_filial.html'
    success_url = reverse_lazy('filiais:lista')

class DetalheFilialView(DetailView):
    model = Filial
    template_name = 'filiais/detalhe_filial.html'

class ExcluiFilialView(DeleteView):
    model = Filial
    template_name = 'filiais/confirmar_exclusao_filial.html'
    success_url = reverse_lazy('filiais:lista')

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm  # Crie um ClienteForm

class ListaClientesView(ListView):
    model = Cliente
    template_name = 'clientes/lista_clientes.html'

class CriaClienteView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/criar_cliente.html'
    success_url = reverse_lazy('clientes:lista')

class EditaClienteView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/editar_cliente.html'
    success_url = reverse_lazy('clientes:lista')

class DetalheClienteView(DetailView):
    model = Cliente
    template_name = 'clientes/detalhe_cliente.html'

class ExcluiClienteView(DeleteView):
    model = Cliente
    template_name = 'clientes/confirmar_exclusao_cliente.html'
    success_url = reverse_lazy('clientes:lista')

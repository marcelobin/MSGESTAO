from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Usuario
from .forms import UsuarioForm

class ListaUsuariosView(ListView):
    model = Usuario
    template_name = 'usuarios/lista_usuarios.html'

class CriaUsuarioView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/criar_usuario.html'
    success_url = reverse_lazy('usuarios:lista')

class EditaUsuarioView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/editar_usuario.html'
    success_url = reverse_lazy('usuarios:lista')

class DetalheUsuarioView(DetailView):
    model = Usuario
    template_name = 'usuarios/detalhe_usuario.html'

class ExcluiUsuarioView(DeleteView):
    model = Usuario
    template_name = 'usuarios/confirmar_exclusao_usuario.html'
    success_url = reverse_lazy('usuarios:lista')

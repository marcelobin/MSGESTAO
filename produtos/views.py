from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Produto
from .forms import ProdutoForm  # Crie um ModelForm simples para Produto

class ListaProdutosView(ListView):
    model = Produto
    template_name = 'produtos/lista_produtos.html'

class CriaProdutoView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/criar_produto.html'
    success_url = reverse_lazy('produtos:lista')

class EditaProdutoView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/editar_produto.html'
    success_url = reverse_lazy('produtos:lista')

class DetalheProdutoView(DetailView):
    model = Produto
    template_name = 'produtos/detalhe_produto.html'

class ExcluiProdutoView(DeleteView):
    model = Produto
    template_name = 'produtos/confirmar_exclusao_produto.html'
    success_url = reverse_lazy('produtos:lista')

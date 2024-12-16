from django.urls import path
from .views import (
    ListaProdutosView, CriaProdutoView, EditaProdutoView, DetalheProdutoView, ExcluiProdutoView
)

app_name = 'produtos'

urlpatterns = [
    path('', ListaProdutosView.as_view(), name='lista'),
    path('criar/', CriaProdutoView.as_view(), name='criar'),
    path('editar/<int:pk>/', EditaProdutoView.as_view(), name='editar'),
    path('detalhe/<int:pk>/', DetalheProdutoView.as_view(), name='detalhe'),
    path('excluir/<int:pk>/', ExcluiProdutoView.as_view(), name='excluir'),
]

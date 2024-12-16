from django.urls import path
from .views import (
    ListaClientesView, CriaClienteView, EditaClienteView, DetalheClienteView, ExcluiClienteView
)

app_name = 'clientes'

urlpatterns = [
    path('', ListaClientesView.as_view(), name='lista'),
    path('criar/', CriaClienteView.as_view(), name='criar'),
    path('editar/<int:pk>/', EditaClienteView.as_view(), name='editar'),
    path('detalhe/<int:pk>/', DetalheClienteView.as_view(), name='detalhe'),
    path('excluir/<int:pk>/', ExcluiClienteView.as_view(), name='excluir'),
]

from django.urls import path
from .views import (
    ListaUsuariosView, CriaUsuarioView, EditaUsuarioView, DetalheUsuarioView, ExcluiUsuarioView
)

app_name = 'usuarios'

urlpatterns = [
    path('', ListaUsuariosView.as_view(), name='lista'),
    path('criar/', CriaUsuarioView.as_view(), name='criar'),
    path('editar/<int:pk>/', EditaUsuarioView.as_view(), name='editar'),
    path('detalhe/<int:pk>/', DetalheUsuarioView.as_view(), name='detalhe'),
    path('excluir/<int:pk>/', ExcluiUsuarioView.as_view(), name='excluir'),
]

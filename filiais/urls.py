from django.urls import path
from .views import (
    ListaFiliaisView, CriaFilialView, EditaFilialView, DetalheFilialView, ExcluiFilialView
)

app_name = 'filiais'

urlpatterns = [
    path('', ListaFiliaisView.as_view(), name='lista'),
    path('criar/', CriaFilialView.as_view(), name='criar'),
    path('editar/<int:pk>/', EditaFilialView.as_view(), name='editar'),
    path('detalhe/<int:pk>/', DetalheFilialView.as_view(), name='detalhe'),
    path('excluir/<int:pk>/', ExcluiFilialView.as_view(), name='excluir'),
]

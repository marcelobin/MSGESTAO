from django.urls import path
from . import views

app_name = 'lojas'

urlpatterns = [
    path('', views.lista_lojas, name='lista'),
    path('criar/', views.criar_loja, name='criar'),
    path('editar/<int:pk>/', views.editar_loja, name='editar'),
    path('detalhe/<int:pk>/', views.detalhe_loja, name='detalhe'),
    path('excluir/<int:pk>/', views.excluir_loja, name='excluir'),
]

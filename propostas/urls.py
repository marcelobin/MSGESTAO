from django.urls import path
from . import views

app_name = 'propostas'

urlpatterns = [
    path('', views.lista_propostas, name='lista'),
    path('criar/', views.criar_proposta, name='criar'),
    path('editar/<int:pk>/', views.editar_proposta, name='editar'),
    path('detalhe/<int:pk>/', views.detalhe_proposta, name='detalhe'),
    path('excluir/<int:pk>/', views.excluir_proposta, name='excluir'),
]

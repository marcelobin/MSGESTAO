from django.urls import path
from .views import (
    ListaLancamentosView, CriaLancamentoView, EditaLancamentoView, DetalheLancamentoView, ExcluiLancamentoView
)

app_name = 'financeiro'

urlpatterns = [
    path('', ListaLancamentosView.as_view(), name='lista'),
    path('criar/', CriaLancamentoView.as_view(), name='criar'),
    path('editar/<int:pk>/', EditaLancamentoView.as_view(), name='editar'),
    path('detalhe/<int:pk>/', DetalheLancamentoView.as_view(), name='detalhe'),
    path('excluir/<int:pk>/', ExcluiLancamentoView.as_view(), name='excluir'),
]

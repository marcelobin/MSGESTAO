from django.urls import path
from .views import (
    ListaFinanceirasView, CriaFinanceiraView, EditaFinanceiraView, DetalheFinanceiraView, ExcluiFinanceiraView
)

app_name = 'financeiras'

urlpatterns = [
    path('', ListaFinanceirasView.as_view(), name='lista'),
    path('criar/', CriaFinanceiraView.as_view(), name='criar'),
    path('editar/<int:pk>/', EditaFinanceiraView.as_view(), name='editar'),
    path('detalhe/<int:pk>/', DetalheFinanceiraView.as_view(), name='detalhe'),
    path('excluir/<int:pk>/', ExcluiFinanceiraView.as_view(), name='excluir'),
]

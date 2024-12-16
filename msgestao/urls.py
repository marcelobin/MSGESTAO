from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_dashboard(request):
    return redirect('dashboard:index')  # Ajuste conforme nome do namespace/url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_dashboard, name='home'),
    path('filiais/', include('filiais.urls', namespace='filiais')),
    path('financeiras/', include('financeiras.urls', namespace='financeiras')),
    path('produtos/', include('produtos.urls', namespace='produtos')),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('lojas/', include('lojas.urls', namespace='lojas')),
    path('clientes/', include('clientes.urls', namespace='clientes')),
    path('propostas/', include('propostas.urls', namespace='propostas')),
    path('financeiro/', include('financeiro.urls', namespace='financeiro')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
]

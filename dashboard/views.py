from django.shortcuts import render
from propostas.models import Proposta

def dashboard_view(request):
    # Exemplo simples
    propostas = Proposta.objects.all()
    total_propostas = propostas.count()
    soma_valor = sum([p.valor_financiado for p in propostas])
    context = {
        'total_propostas': total_propostas,
        'soma_valor': soma_valor,
    }
    return render(request, 'dashboard/dashboard.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Proposta
from .forms import PropostaForm, VeiculoForm
from clientes.forms import ClienteForm

def criar_proposta(request):
    if request.method == 'POST':
        pform = PropostaForm(request.POST)
        vform = VeiculoForm(request.POST)
        cform = ClienteForm(request.POST)

        if pform.is_valid() and vform.is_valid() and cform.is_valid():
            # Salva primeiro o cliente
            cliente = cform.save()

            # Salva o veículo
            veiculo = vform.save()

            # Agora cria a proposta vinculada ao cliente e veículo
            proposta = pform.save(commit=False)
            proposta.cliente = cliente
            proposta.veiculo = veiculo
            proposta.save()

            return redirect('propostas:lista')
    else:
        pform = PropostaForm()
        vform = VeiculoForm()
        cform = ClienteForm()

    return render(request, 'propostas/criar_proposta.html', {
        'pform': pform,
        'vform': vform,
        'cform': cform
    })

def lista_propostas(request):
    propostas = Proposta.objects.all()
    return render(request, 'propostas/lista_propostas.html', {'propostas': propostas})


def editar_proposta(request, pk):
    proposta = get_object_or_404(Proposta, pk=pk)
    veiculo = proposta.veiculo
    if request.method == 'POST':
        pform = PropostaForm(request.POST, instance=proposta)
        vform = VeiculoForm(request.POST, instance=veiculo)
        if pform.is_valid() and vform.is_valid():
            vform.save()
            pform.save()
            return redirect('propostas:lista')
    else:
        pform = PropostaForm(instance=proposta)
        vform = VeiculoForm(instance=veiculo)
    return render(request, 'propostas/editar_proposta.html', {'pform': pform, 'vform': vform})

def detalhe_proposta(request, pk):
    proposta = get_object_or_404(Proposta, pk=pk)
    return render(request, 'propostas/detalhe_proposta.html', {'proposta': proposta})

def excluir_proposta(request, pk):
    proposta = get_object_or_404(Proposta, pk=pk)
    if request.method == 'POST':
        proposta.veiculo.delete()
        proposta.delete()
        return redirect('propostas:lista')
    return render(request, 'propostas/confirmar_exclusao_proposta.html', {'proposta': proposta})

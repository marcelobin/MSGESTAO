from django.shortcuts import render, redirect, get_object_or_404
from .models import Loja
from .forms import LojaForm, SocioFormSet, VendedorFormSet
from django.urls import reverse

def lista_lojas(request):
    lojas = Loja.objects.all()
    return render(request, 'lojas/lista_lojas.html', {'lojas': lojas})

def criar_loja(request):
    if request.method == "POST":
        form = LojaForm(request.POST)
        socio_formset = SocioFormSet(request.POST)
        vendedor_formset = VendedorFormSet(request.POST)
        if form.is_valid() and socio_formset.is_valid() and vendedor_formset.is_valid():
            loja = form.save()
            socio_formset.instance = loja
            vendedor_formset.instance = loja
            socio_formset.save()
            vendedor_formset.save()
            return redirect('lojas:lista')
    else:
        form = LojaForm()
        socio_formset = SocioFormSet()
        vendedor_formset = VendedorFormSet()
    return render(request, 'lojas/criar_loja.html', {
        'form': form,
        'socio_formset': socio_formset,
        'vendedor_formset': vendedor_formset,
    })

def editar_loja(request, pk):
    loja = get_object_or_404(Loja, pk=pk)
    if request.method == "POST":
        form = LojaForm(request.POST, instance=loja)
        socio_formset = SocioFormSet(request.POST, instance=loja)
        vendedor_formset = VendedorFormSet(request.POST, instance=loja)
        if form.is_valid() and socio_formset.is_valid() and vendedor_formset.is_valid():
            form.save()
            socio_formset.save()
            vendedor_formset.save()
            return redirect('lojas:lista')
    else:
        form = LojaForm(instance=loja)
        socio_formset = SocioFormSet(instance=loja)
        vendedor_formset = VendedorFormSet(instance=loja)
    return render(request, 'lojas/editar_loja.html', {
        'form': form,
        'socio_formset': socio_formset,
        'vendedor_formset': vendedor_formset,
    })

def detalhe_loja(request, pk):
    loja = get_object_or_404(Loja, pk=pk)
    return render(request, 'lojas/detalhe_loja.html', {'loja': loja})

def excluir_loja(request, pk):
    loja = get_object_or_404(Loja, pk=pk)
    if request.method == "POST":
        loja.delete()
        return redirect('lojas:lista')
    return render(request, 'lojas/confirmar_exclusao_loja.html', {'loja': loja})

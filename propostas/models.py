from django.db import models
from clientes.models import Cliente
from lojas.models import Loja, Vendedor
from usuarios.models import Usuario
from financeiras.models import Financeira

class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    id_veiculo = models.AutoField(primary_key=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=10)
    renavam = models.CharField(max_length=20)
    chassi = models.CharField(max_length=30)
    valor_veiculo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.marca.nome} - {self.modelo} [{self.placa}]"

class Proposta(models.Model):
    id_proposta = models.AutoField(primary_key=True)
    nro_proposta = models.CharField(max_length=50, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    financeira = models.ForeignKey(Financeira, on_delete=models.CASCADE)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    contato_comercial = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    valor_financiado = models.DecimalField(max_digits=10, decimal_places=2)
    prazo = models.PositiveIntegerField()
    veiculo = models.OneToOneField(Veiculo, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Proposta {self.nro_proposta}"

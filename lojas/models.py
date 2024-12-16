from django.db import models
from filiais.models import Filial
from usuarios.models import Usuario

class Loja(models.Model):
    id_loja = models.AutoField(primary_key=True)
    cnpj = models.CharField(max_length=18, unique=True)
    razao_social = models.CharField(max_length=200)
    nome_fantasia = models.CharField(max_length=200)
    data_constituicao = models.DateField()
    cep = models.CharField(max_length=10)
    endereco = models.CharField(max_length=200)
    nro = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    filial = models.ForeignKey(Filial, on_delete=models.SET_NULL, null=True, blank=True)
    contato_comercial = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True,
                                          limit_choices_to={'funcao__in': ['CCE', 'CCI', 'ADMIN']})

    def __str__(self):
        return self.nome_fantasia

class Socio(models.Model):
    id_socio = models.AutoField(primary_key=True)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name='socios')
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.loja.nome_fantasia}"

class Vendedor(models.Model):
    id_vendedor = models.AutoField(primary_key=True)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name='vendedores')
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    chave_pix = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.loja.nome_fantasia}"

from django.db import models
from filiais.models import Filial

# Funções possíveis: Administrador, Contato Comercial Externo, Contato Comercial Interno
FUNCOES = (
    ('ADMIN', 'Administrador'),
    ('CCE', 'Contato Comercial Externo'),
    ('CCI', 'Contato Comercial Interno')
)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    funcao = models.CharField(max_length=5, choices=FUNCOES)
    filial = models.ForeignKey(Filial, on_delete=models.SET_NULL, null=True, blank=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nome

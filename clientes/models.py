from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    nome_mae = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome

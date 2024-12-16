from django.db import models

class Financeira(models.Model):
    id_financeira = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

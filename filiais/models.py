from django.db import models

class Filial(models.Model):
    id_filial = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

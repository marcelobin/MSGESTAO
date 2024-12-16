from django.db import models
from financeiras.models import Financeira

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    financeira = models.ForeignKey(Financeira, on_delete=models.CASCADE)
    comissao_percentual = models.DecimalField(max_digits=5, decimal_places=2)  # Ex: 1.50 = 1,5%
    
    def __str__(self):
        return f"{self.nome} - {self.financeira.nome}"

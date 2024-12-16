from django.db import models
from filiais.models import Filial

TIPOS_LANCAMENTO = (
    ('R', 'Receita'),
    ('D', 'Despesa'),
)

class LancamentoFinanceiro(models.Model):
    id_lancamento = models.AutoField(primary_key=True)
    filial = models.ForeignKey(Filial, on_delete=models.SET_NULL, null=True, blank=True)
    data = models.DateField()
    tipo = models.CharField(max_length=1, choices=TIPOS_LANCAMENTO)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.descricao} - {self.valor}"

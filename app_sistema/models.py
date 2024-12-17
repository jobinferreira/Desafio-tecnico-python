from django.db import models

class Equipamento(models.Model):
    tipo = models.CharField(max_length=100, null=False, blank=False)
    fabricante = models.CharField(max_length=100, null=False, blank=False)
    modelo = models.CharField(max_length=100, null=False, blank=False)
    numero_serie = models.CharField(max_length=16, null=False, blank=False)
    data_compra = models.DateField(null=True)
    valor_compra = models.IntegerField(null=True)

    def __str__(self):
        return self.tipo


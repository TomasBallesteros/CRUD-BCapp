from __future__ import unicode_literals

from django.db import models

# Create your models here.
class insumo(models.Model):
    codigo = models.CharField(max_length=10)
    nombreI = models.CharField(max_length=100)
    detalle = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    unidad = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=200)

    def __str__(self):
        return self.codigo

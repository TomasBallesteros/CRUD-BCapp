from __future__ import unicode_literals
from django.db import models
from insumo.models import insumo
from obra.models import obra

# Create your models here.
class presupuesto(models.Model):
    idPresupuesto = models.AutoField(primary_key=True)
    codigo = models.ForeignKey(insumo, null=True)
    nit = models.ForeignKey(obra, null=True)
    cantidad = models.IntegerField()
    precoParcial = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.idPresupuesto

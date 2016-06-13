from __future__ import unicode_literals

from django.db import models

# Create your models here.
class obra(models.Model):
    nit = models.CharField(max_length=10)
    nombreO = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    fecha_inicio = models.DateField(auto_now_add=False)
    fecha_fin = models.DateField(auto_now_add=False)
    observacioneso = models.CharField(max_length=200)

    def __str__(self):
        return self.nit

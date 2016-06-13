from django.contrib import admin

# Register your models here.
from .models import insumo

class insumoAdmin(admin.ModelAdmin):
    fields = ['codigo','nombreI','detalle','precio','unidad','observaciones']

admin.site.register(insumo)

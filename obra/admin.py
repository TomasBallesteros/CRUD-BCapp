from django.contrib import admin

# Register your models here.
from .models import obra

class obraAdmin(admin.ModelAdmin):
    fields = ['nit','nombreO','direccion','fecha_inicio','fecha_fin','observacioneso']

admin.site.register(obra)

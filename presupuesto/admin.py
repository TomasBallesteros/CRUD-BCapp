from django.contrib import admin

# Register your models here.
from .models import presupuesto

class presupuestoAdmin(admin.ModelAdmin):
    fields = ['cantidad','precoParcial']

admin.site.register(presupuesto)

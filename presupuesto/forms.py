#encoding:utf-8

from django.forms import ModelForm
from django import forms
from .models import presupuesto
from insumo.models import insumo
from obra.models import obra

class presupuestoForm(forms.ModelForm):
    cantidad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese la cantidad'}))
    precoParcial = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese el precio parcial'}))
    codigo_id = forms.ModelChoiceField(queryset=insumo.objects.all(), initial=0, to_field_name="codigo")
    nit_id = forms.ModelChoiceField(queryset=obra.objects.all(), initial=0, to_field_name="nit")

    class Meta:
        model = presupuesto
        fields = ['cantidad','precoParcial','codigo_id','nit_id']

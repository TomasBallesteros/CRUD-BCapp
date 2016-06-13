#encoding:utf-8

from django.forms import ModelForm
from django import forms
from .models import insumo

class insumoForm(forms.ModelForm):
    codigo = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese el codigo'}))
    nombreI = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese el nombre'}))
    detalle = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese el detalle'}))
    precio = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese el precio'}))
    unidad = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese la unidad de medida'}))
    observaciones = forms.CharField(widget=forms.Textarea(attrs={'class': 'error','placeholder': 'Ingrese observaciones'}))

    class Meta:
        model = insumo
        fields = ['codigo','nombreI','detalle','precio','unidad','observaciones']

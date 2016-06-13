#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import obra

class obraForm(forms.ModelForm):
    nit = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese el nit'}))
    nombreO = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese el nombre'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese la direccion'}))
    fecha_inicio = forms.DateField(widget=forms.SelectDateWidget())
    fecha_fin = forms.DateField(widget=forms.SelectDateWidget())
    observacioneso = forms.CharField(widget=forms.Textarea(attrs={'class': 'error','placeholder': 'Ingrese observaciones'}))

    class Meta:
        model = obra
        fields = ['nit','nombreO','direccion','fecha_inicio','fecha_fin','observacioneso']

#coding=utf-8
from django import forms
from .models import Compra, TotalVendido

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        exclude = []

class TotalVendidoForm(forms.ModelForm):
    class Meta:
        model = TotalVendido
        exclude = []

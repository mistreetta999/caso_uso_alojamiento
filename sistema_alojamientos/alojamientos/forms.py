"""
forms.py - Formularios para la app alojamientos
"""
from django import forms
from .models import Alojamiento

class AlojamientoForm(forms.ModelForm):
    class Meta:
        model = Alojamiento
        fields = ["nombre", "direccion", "capacidad", "precio", "disponible"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            "capacidad": forms.NumberInput(attrs={"class": "form-control"}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "disponible": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

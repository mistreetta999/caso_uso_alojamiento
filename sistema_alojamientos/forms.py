# sistema_alojamientos/forms.py
from django import forms
from .models import Alojamiento

class AlojamientoForm(forms.ModelForm):
    class Meta:
        model = Alojamiento
        fields = ["nombre", "capacidad", "precio"]

        # Opcional: etiquetas y estilos
        labels = {
            "nombre": "Nombre del alojamiento",
            "capacidad": "Capacidad máxima",
            "precio": "Precio por noche",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "capacidad": forms.NumberInput(attrs={"class": "form-control"}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }

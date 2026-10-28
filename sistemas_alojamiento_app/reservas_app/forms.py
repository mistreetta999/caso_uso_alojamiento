from django import forms
from .models import Reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            "cliente",
            "cabana",
            "fecha_inicio",
            "fecha_fin",
            "hora_ingreso",
            "hora_salida",
        ]

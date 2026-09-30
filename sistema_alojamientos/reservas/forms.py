"""Formularios para la aplicación de reservas."""

from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    """Formulario para la creación y edición de reservas."""
    class Meta:
        """Metadatos del formulario Reserva."""
        model = Reserva
        fields = [
            "cliente",
            "cabana",
            "fecha_ingreso",
            "fecha_salida",
            "observaciones",
        ]
        widgets = {
            "fecha_ingreso": forms.DateInput(attrs={"type": "date"}),
            "fecha_salida": forms.DateInput(attrs={"type": "date"}),
            "hora_ingreso": forms.TimeInput(attrs={"type": "time"}),
            "hora_salida": forms.TimeInput(attrs={"type": "time"}),
            "observaciones": forms.Textarea(attrs={"rows": 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_ingreso = cleaned_data.get("fecha_ingreso")
        fecha_salida = cleaned_data.get("fecha_salida")

        if fecha_ingreso and fecha_salida and fecha_ingreso > fecha_salida:
            raise forms.ValidationError("La fecha de ingreso no puede ser posterior a la fecha de salida.")

        return cleaned_data

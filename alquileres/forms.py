"""Formularios para la aplicación de alquileres."""
from django import forms
from . import models

Cabana = getattr(models, "Cabana")

class CabanaForm(forms.ModelForm):
    """Formulario para el modelo Cabana."""
    class Meta:
        """Metadatos del modelo Cabana."""
        model = Cabana
        fields = '__all__'

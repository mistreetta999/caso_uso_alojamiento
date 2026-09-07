"""Formulario para la aplicación de cabañas."""

from django import forms  # type: ignore[import-not-found]
from .models import Cabana

class CabanaForm(forms.ModelForm):
    """ class fromulario"""
    class Meta:
        """ class meta"""
        model = Cabana   # ✅ tu modelo real
        fields = '__all__'

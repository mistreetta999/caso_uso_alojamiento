from django import forms
from .models import Cabana

class CabanaForm(forms.ModelForm):
    class Meta:
        model = Cabana
        fields = ["nombre", "ubicacion", "capacidad"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "ubicacion": forms.TextInput(attrs={"class": "form-control"}),
            "capacidad": forms.NumberInput(attrs={"class": "form-control"}),
        }

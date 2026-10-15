from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["cliente", "alojamiento", "fecha_inicio", "fecha_fin"]
        widgets = {
            "cliente": forms.Select(attrs={"class": "form-control"}),
            "alojamiento": forms.Select(attrs={"class": "form-control"}),
            "fecha_inicio": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "fecha_fin": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }

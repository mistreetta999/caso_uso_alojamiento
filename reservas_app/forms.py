from django import forms
from reservas_app.models import Reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["cliente", "cabana", "fecha_inicio", "fecha_fin", "hora_ingreso", "hora_salida"]
        widgets = {
            "cliente": forms.Select(attrs={"class": "form-control"}),
            "cabana": forms.Select(attrs={"class": "form-control"}),
            "fecha_inicio": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "fecha_fin": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "hora_ingreso": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "hora_salida": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
        }

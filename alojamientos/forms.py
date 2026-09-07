"""Formularios para la aplicación de alojamientos."""
from django import forms as django_forms
from django.shortcuts import render
from alquileres.models import Alquileres
from clientes.models import Cliente 
from cabanas.models import Cabana
def forms(request):
    return render(request, 'template_name.html', {'form': AlquilerForm()})
class AlquilerForm(django_forms.Form):
    """
    Formulario para registrar un alquiler de cabaña.
    """
    cliente = django_forms.ModelChoiceField(queryset=Cliente.objects.all(), label="Cliente")
    cabana = django_forms.ModelChoiceField(queryset=Cabana.objects.all(), label="Cabaña")
    fecha_ingreso = django_forms.DateField(widget=django_forms.DateInput(attrs={'type': 'date'}), label="Fecha de entrada")
    hora_ingreso = django_forms.TimeField(widget=django_forms.TimeInput(attrs={'type': 'time'}), label="Hora de entrada")
    fecha_salida = django_forms.DateField(widget=django_forms.DateInput(attrs={'type': 'date'}), label="Fecha de salida")
    hora_salida = django_forms.TimeField(widget=django_forms.TimeInput(attrs={'type': 'time'}), label="Hora de salida")
    
    def clean(self):
        cleaned_data = super().clean()
        fecha_ingreso = cleaned_data.get("fecha_ingreso")
        fecha_salida = cleaned_data.get("fecha_salida")

        if fecha_ingreso and fecha_salida:
            if fecha_salida < fecha_ingreso:
                raise django_forms.ValidationError("La fecha de salida no puede ser anterior a la fecha de entrada.")

        return cleaned_data
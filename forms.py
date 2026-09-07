from django import forms
from .models import Cabana

class CabanaForm(forms.ModelForm):
    class Meta:
        model = Cabana
        fields = '__all__' # Toma automáticamente todos los campos del modelo de cabaña

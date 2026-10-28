from django.contrib import admin
from .models import Alojamiento

@admin.register(Alojamiento)
class AlojamientoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_noche', 'capacidad', 'disponible')


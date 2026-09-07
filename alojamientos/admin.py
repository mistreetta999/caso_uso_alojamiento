"""Admin configuration for the alojamientos app."""
from django.contrib import admin
from .models import Alojamiento

@admin.register(Alojamiento)
class AlojamientoAdmin(admin.ModelAdmin):
    """Admin configuration for the Alojamiento model."""
    list_display = ("nombre", "direccion", "capacidad", "precio")

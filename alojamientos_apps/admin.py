"""Administración de la aplicación de alojamientos."""
from django.contrib import admin
from .models import Alojamiento

@admin.register(Alojamiento)
class AlojamientoAdmin(admin.ModelAdmin):
    pass

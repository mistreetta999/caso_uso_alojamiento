"""Configuración del administrador para la aplicación de alojamientos."""   
from django.contrib import admin
from .models import Alojamiento

@admin.register(Alojamiento)
class AlojamientoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "capacidad", "precio_por_noche")

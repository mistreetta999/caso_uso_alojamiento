from django.contrib import admin
from .models import Alojamiento

@admin.register(Alojamiento)
class AlojamientoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio_por_noche", "capacidad", "ubicacion")
    search_fields = ("nombre", "ubicacion")
    list_filter = ("ubicacion", "capacidad")

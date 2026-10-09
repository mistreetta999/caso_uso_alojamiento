from django.contrib import admin
from .models import Alojamiento

@admin.register(Alojamiento)
class AlojamientoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "capacidad", "precio")
    search_fields = ("nombre",)
    list_filter = ("capacidad",)

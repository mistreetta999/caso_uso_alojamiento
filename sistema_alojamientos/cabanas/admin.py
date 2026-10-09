from django.contrib import admin
from .models import Cabana

@admin.register(Cabana)
class CabanaAdmin(admin.ModelAdmin):
    """Admin interface for the Cabana model."""
    list_display = ["id", "nombre", "capacidad", "precio"]
    list_filter = ["capacidad", "precio"]

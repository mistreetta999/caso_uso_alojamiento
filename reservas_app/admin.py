from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("cliente", "fecha_reserva", "cantidad_personas")
    search_fields = ("cliente",)
    list_filter = ("fecha_reserva",)

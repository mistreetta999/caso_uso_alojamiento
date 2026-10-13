from django.contrib import admin
from sistema_alojamientos.clientes.models import Cliente
from sistema_alojamientos.reservas.models import Reserva
from sistema_alojamientos.cabanas.models import Cabana
from sistema_alojamientos.alojamientos.models import Alojamiento

# Configuración centralizada del admin

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email")
    search_fields = ("nombre", "apellido", "email")

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("cliente", "fecha_inicio", "fecha_fin", "estado")
    list_filter = ("estado", "fecha_inicio")

@admin.register(Cabana)
class CabanaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "capacidad", "precio")
    search_fields = ("nombre",)

@admin.register(Alojamiento)
class AlojamientoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ubicacion", "tipo")
    search_fields = ("nombre", "ubicacion")

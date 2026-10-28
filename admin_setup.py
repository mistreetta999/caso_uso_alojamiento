from django.contrib import admin
from sistema_alojamientos.clientes.models import Cliente
from sistema_alojamientos.reservas.models import Reserva
from sistema_alojamientos.cabanas.models import Cabana


# Importa los modelos desde sus respectivas apps
from clientes_app.models import Cliente
from sistemas_alojamiento_app.reservas_app.models import Reserva
from sistemas_alojamiento_app.cabanas_app.models import Cabana
from alojamientos_app.models import Alojamiento

# Configuración centralizada del panel de administración de Django

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

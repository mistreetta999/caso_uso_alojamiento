from django.contrib import admin

# Importá aquí los modelos principales de tu proyecto
# Ejemplo: si tenés un modelo Alojamiento en la app alojamientos
from sistema_alojamientos.alojamientos.models import Alojamiento

@admin.register(Alojamiento)
class AlojamientoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ubicacion", "precio", "disponible")
    search_fields = ("nombre", "ubicacion")
    list_filter = ("disponible",)

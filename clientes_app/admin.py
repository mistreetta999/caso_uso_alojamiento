from django.contrib import admin
from .models import Cliente

# cspell:ignore Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """Configuración del modelo Cliente en el panel de administración."""
    list_display = ("nombre", "apellido", "id", "telefono")
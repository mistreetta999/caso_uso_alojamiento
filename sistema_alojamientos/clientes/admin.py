"""Configuración del administrador para la aplicación de clientes."""
from django.contrib import admin
from .models import Cliente

admin.site.register(Cliente)

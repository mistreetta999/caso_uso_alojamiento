""" urls.py - Configuración de URLs del proyecto de alojamientos. """
from typing import Any

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
def inicio(_request: Any) -> HttpResponse:
    """Vista de inicio que muestra un mensaje de bienvenida.""" 
    return HttpResponse('Bienvenido a Alojamientos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('alojamientos.urls', 'alojamientos'), namespace='alojamientos')),
        # Rutas de tus aplicaciones secundarias
    path('clientes/', include(('clientes.urls', 'clientes'), namespace='clientes')),
    path('cabanas/', include(('cabanas.urls', 'cabanas'), namespace='cabanas')),
    path('alquileres/', include(('alquileres.urls', 'alquileres'), namespace='alquileres'))
]   
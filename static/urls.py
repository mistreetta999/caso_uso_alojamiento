"""
urls.py para sistema_alojamientos
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #  rutas de django
    path('clientes/', include('sistema_alojamientos.clientes.urls')),
    path('reservas/', include('sistema_alojamientos.reservas.urls')),
    path('alojamientos/', include('sistema_alojamientos.alojamientos.urls')),
    path('cabanas/', include('sistema_alojamientos.cabanas.urls')),
        path('admin/', admin.site.urls),
    #  rutas de tus apps
    path('clientes_app/', include('sistema_alojamientos.clientes.urls')),
    path('reservas_app/', include('sistema_alojamientos.reservas.urls')),
    path('alojamientos_app/', include('sistema_alojamientos.alojamientos.urls')),
    path('cabanas_app/', include('sistema_alojamientos.cabanas.urls'


]


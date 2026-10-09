"""
urls.py para sistema_alojamientos
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #  rutas de tus apps
    path('clientes/', include('sistema_alojamientos.clientes.urls')),
    path('reservas/', include('sistema_alojamientos.reservas.urls')),
    path('alojamientos/', include('sistema_alojamientos.alojamientos.urls')),
    path('cabanas/', include('sistema_alojamientos.cabanas.urls')),


]

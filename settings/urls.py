"""
URLs principales del sistema de alojamientos.
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from rest_framework import routers
from alojamientos_app.views import (
    ClienteViewSet, 
    ReservaViewSet, 
    AlojamientoViewSet, 
)
from cabanas.views import CabanaViewSet
from sistema_alojamientos.views import sistema_unificado

def dashboard(request):
    """Renderiza la página principal del dashboard."""
    return render(request, "dashboard.html")

# Configuración del enrutador de la API (DRF)
router = routers.DefaultRouter()
router.register(r"clientes", ClienteViewSet)
router.register(r"cabanas", CabanaViewSet)
router.register(r"reservas", ReservaViewSet)
router.register(r"alojamientos", AlojamientoViewSet)

urlpatterns = [
    # Panel de administración de Django
    path("admin/", admin.site.urls),
    
    # Endpoints de la API REST
    path("api/", include(router.urls)),

    # Dashboard principal
    path("", dashboard, name="dashboard"),

    # Rutas de las aplicaciones del sistema
    path("alojamientos/", include("sistema_alojamientos.alojamientos.urls")),
    path("cabanas/", include("sistema_alojamientos.cabanas.urls")),
    path("reservas/", include("sistema_alojamientos.reservas.urls")),
    path("clientes/", include("clientes_app.urls")),

    # Vista del sistema unificado
    path("sistema/", sistema_unificado, name="sistema_unificado"),
]
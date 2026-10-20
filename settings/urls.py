"""
URLs principales del sistema de alojamientos.
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from rest_framework import routers

# Importar cada ViewSet desde su app correspondiente
from clientes_app.views import ClienteViewSet
from reservas_app.views import ReservaViewSet
from alojamientos_app.views import AlojamientoViewSet
from cabanas_app.views import CabanaViewSet
from sistema_alojamientos.views import sistema_unificado  # si realmente existe

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
    path("alojamientos/", include("alojamientos_app.urls")),
    path("cabanas/", include("cabanas_app.urls")),
    path("reservas/", include("reservas_app.urls")),
    path("clientes/", include("clientes_app.urls")),

    # Vista del sistema unificado
    path("sistema/", sistema_unificado, name="sistema_unificado"),
]

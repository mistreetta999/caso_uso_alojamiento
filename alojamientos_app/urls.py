"""
URLs del módulo de sistema_alojamientos.
"""
from django.shortcuts import render

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from alojamientos_app.views import AlojamientoViewSet, InicioView, SistemaUnificadoView, crear_alojamiento
from cabanas_app.views import CabanaViewSet
from clientes_app.views import ClienteViewSet
from reservas_app.views import ReservaViewSet

def dashboard(request):
    """Renderiza la página principal del dashboard."""
    return render(request, "dashboard.html")

router = routers.DefaultRouter()
router.register(r"clientes", ClienteViewSet)
router.register(r"cabanas", CabanaViewSet)
router.register(r"reservas", ReservaViewSet)
router.register(r"alojamientos", AlojamientoViewSet)

app_name = "alojamientos"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
     path("alojamientos/nuevo/", crear_alojamiento, name="crear_alojamiento"),
    # Dashboard principal
    path("", dashboard, name="dashboard"),
    path("inicio/", InicioView.as_view(), name="inicio"),

    # Sistema unificado
    path("sistema/", SistemaUnificadoView.as_view(), name="sistema_unificado"),

    # Apps del sistema
    path("alojamientos/", include("alojamientos_app.urls")),
    path("cabanas/", include("cabanas_app.urls")),
    path("reservas/", include("reservas_app.urls")),
    path("clientes/", include("clientes_app.urls")),
    path("alojamientos/", include("sistema_alojamientos.alojamientos_app.urls")),
    path("cabanas/", include("sistema_alojamientos.cabanas_app.urls")),
    path("reservas/", include("sistema_alojamientos.reservas_app.urls")),
    path("clientes/", include("sistema_alojamientos.clientes_app.urls")),
]


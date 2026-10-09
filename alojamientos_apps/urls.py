from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from rest_framework import routers
from sistema_alojamientos.clientes.views import ClienteViewSet
from sistema_alojamientos.cabanas.views import CabanaViewSet
from sistema_alojamientos.reservas.views import ReservaViewSet
from sistema_alojamientos.alojamientos.views import AlojamientoViewSet
def dashboard(request):
    """Renderiza la página principal del dashboard."""
    return render(request, "dashboard.html")
router = routers.DefaultRouter()
router.register(r"clientes", ClienteViewSet)
router.register(r"cabanas", CabanaViewSet)
router.register(r"reservas", ReservaViewSet)
router.register(r"alojamientos", AlojamientoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("", dashboard, name="dashboard"),
    path("alojamientos/", include("sistema_alojamientos.alojamientos.urls")),
    path("cabanas/", include("sistema_alojamientos.cabanas.urls")),
    path("reservas/", include("sistema_alojamientos.reservas.urls")),
    path("clientes/", include("sistema_alojamientos.clientes.urls")),   
    path("template/", include("sistema_alojamientos.template.urls")),
]

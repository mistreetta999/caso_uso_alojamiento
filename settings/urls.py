"""
URLs principales del sistema de alojamientos.
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rest_framework import routers

# Importar cada ViewSet desde su app correspondiente

from clientes_app.views import ClienteViewSet
from sistemas_alojamiento_app.reservas_app.views import ReservaViewSet
from alojamientos_app.views import AlojamientoViewSet
from sistemas_alojamiento_app.cabanas_app.views import CabanaViewSet
from sistema_alojamientos.views import sistema_unificado 
def get_router():
    router = routers.DefaultRouter()
    router.register(r'reservas', ReservaViewSet)
    router.register(r'clientes', ClienteViewSet)
    router.register(r'cabanas', CabanaViewSet)
    router.register(r'alojamientos', AlojamientoViewSet)
    return router
# Router DRF
router = routers.DefaultRouter()
router.register(r'reservas', ReservaViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'cabanas', CabanaViewSet)
router.register(r'alojamientos', AlojamientoViewSet)
def  clientes_views(request):
    return render(request,clientes_views.html)
def alojamientos_app_view(request):
    return render(request, 'alojamientos_app.html') 

def respuesta_root(request):
    return render(request, "respuesta_root.html")


def sistema_unificado(request: HttpRequest) -> HttpResponse:
    return render(request, "sistema_unificado.html")


def dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, "alojamientos/global/global/dashboard.html")



# si realmente existe
def clientes_views_set(request):
    """Vista para la sección de clientes."""
    return render(request, "global/global/clientes.html")
def reservas_views_set(request):
    """Vista para la sección de reservas."""
    return render(request, "global/global/reservas.html")
def alojamientos_views_set(request):
    """Vista para la sección de alojamientos."""
    return render(request, "global/global/alojamientos.html")   
# API REST para clientes.
def api_clientes(request):
    """Endpoint de la API REST para clientes."""
    return render(request, "global/global/api_clientes.html")   
def dashboard(request):
    """Renderiza la página principal del dashboard."""
    return render(request, "global/global/dashboard.html")
def sistema_unificado(request):
    """Vista principal o unificada del sistema."""
    return render(request, "global/global/sistema_unificado.html")
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


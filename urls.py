from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from alojamientos_app.views import AlojamientoViewSet, crear_alojamiento
from cabanas_app.views import CabanaViewSet
from clientes_app.views import ClienteViewSet
from reservas_app.views import ReservaViewSet
from .render import dashboard, inicio, sistema_unificado

router = DefaultRouter()
router.register(r"clientes", ClienteViewSet)
router.register(r"cabanas", CabanaViewSet)
router.register(r"reservas", ReservaViewSet)
router.register(r"alojamientos", AlojamientoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),

    # Dashboard global
    path("", dashboard, name="dashboard"),
    path("inicio/", inicio, name="inicio"),
    path("sistema/", sistema_unificado, name="sistema_unificado"),

    # CRUD alojamientos
    path("alojamientos/nuevo/", crear_alojamiento, name="crear_alojamiento"),

    # Apps del sistema
    path("alojamientos/", include("alojamientos_app.urls")),
    path("cabanas/", include("cabanas_app.urls")),
    path("reservas/", include("reservas_app.urls")),
    path("clientes/", include("clientes_app.urls")),
]

from django.urls import path, include
from rest_framework import routers

from clientes_app.views import ClienteViewSet
from reservas_app.views import ReservaViewSet
from cabanas_app.views import CabanaViewSet
from alojamientos_app.views import AlojamientoViewSet
from reservas_app import views  # para index y crear_reserva

# Router DRF
router = routers.DefaultRouter()
router.register(r'reservas', ReservaViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'cabanas', CabanaViewSet)
router.register(r'alojamientos', AlojamientoViewSet)

urlpatterns = [
    # Vistas propias de reservas
    path("", views.index, name="reservas_index"),
    path("crear/", views.crear_reserva, name="crear_reserva"),

    # API REST con router
    path("api/", include(router.urls)),
]

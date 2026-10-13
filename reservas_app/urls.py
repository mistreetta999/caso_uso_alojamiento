from django.urls import path
from . import views
from clientes_app.views import ClienteViewSet
from reservas_app.views import ReservaViewSet
from cabanas_app.views import CabanaViewSet
from alojamientos_app.views import AlojamientoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'reservas', ReservaViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'cabanas', CabanaViewSet)
router.register(r'alojamientos', AlojamientoViewSet)
urlpatterns = [
    path("", views.index, name="reservas_index"),
    # Ejemplo de ruta para crear una reserva
    path("crear/", views.index, name="crear_reserva"),


]

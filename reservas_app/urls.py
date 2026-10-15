from django.urls import path, include
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
    path("home/", views.home, name="home"),
    path("router/", include(router.urls)),
    path("clientes/", include(router.urls)),
    path("cabanas/", include(router.urls)),
    path("alojamientos/", include(router.urls)),
    path("reservas/", include(router.urls)),

]

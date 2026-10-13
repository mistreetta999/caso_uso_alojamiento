"""URLs for the clientes_app."""
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from reservas_app.views import ReservaViewSet
from cabanas_app.views import CabanaViewSet
from alojamientos_app.views import AlojamientoViewSet
from .views import ClienteViewSet
router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'cabanas', CabanaViewSet)
router.register(r'alojamientos', AlojamientoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('cliente_reservas/', include(router.urls)),
    path('cliente_detalles/', include(router.urls)),
    path('clientes/', include(router.urls)),
    path('cabanas/', include(router.urls)),
    path('alojamientos/', include(router.urls)),
    path('reservas/', include(router.urls)),
    path('cliente_reservas/', include(router.urls)),
    path('cliente_detalles/', include(router.urls)),
    path('', include(router.urls)),
    
]

urlpatterns += router.urls

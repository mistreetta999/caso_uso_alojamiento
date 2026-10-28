from django.urls import include, path
from rest_framework import routers
from sistemas_alojamiento_app.reservas_app.views import ReservaViewSet, ClienteViewSet, CabanaViewSet, AlojamientoViewSet
 Router 
router = routers.DefaultRouter()
router.register(r'reservas', ReservaViewSet, basename='api_reservas')
router.register(r'clientes', ClienteViewSet, basename='api_clientes')
router.register(r'cabanas', CabanaViewSet, basename='api_cabanas')
router.register(r'alojamientos', AlojamientoViewSet, basename='api_alojamientos')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("clientes/", include("clientes.urls")),
    path("reservas/", include("reservas.urls")),
    path("cabanas/", include("cabanas.urls")),
    path("alojamientos/", include("alojamientos.urls")),

    # Si también usás las apps con sufijo _app
    path("clientes_app/", include("clientes_app.urls")),
    path("reservas_app/", include("reservas_app.urls")),
    path("cabanas_app/", include("cabanas_app.urls")),
    path("alojamientos_app/", include("alojamientos_app.urls")),
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cabanas/", include("sistema_alojamientos.cabanas.urls")),
    path("clientes/", include("sistema_alojamientos.clientes.urls")),
    path("reservas/", include("sistema_alojamientos.reservas.urls")),
    path("alojamientos/", include("alojamientos_apps.urls")),
]

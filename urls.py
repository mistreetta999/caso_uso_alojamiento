"""
URL configuration for the sistema_alojamientos project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),

    # ⚡ Redirigir raíz directamente a reservas (podés cambiarlo a clientes o cabañas)
    path("", RedirectView.as_view(url="/reservas/", permanent=False)),

    # Apps internas
    path("cabanas/", include("sistema_alojamientos.cabanas.urls")),
    path("alojamientos/", include("sistema_alojamientos.alojamientos.urls")),
    path("clientes/", include("sistema_alojamientos.clientes.urls")),
    path("reservas/", include("sistema_alojamientos.reservas.urls")),

    # App externa
    path("alojamientos-apps/", include("alojamientos_apps.urls")),
]

# Archivos estáticos y media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Redirigir cualquier URL no encontrada a la página de inicio de reservas
urlpatterns += [
    path("", RedirectView.as_view(url="/reservas/", permanent=False)),
]
    
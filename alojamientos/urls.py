"""URLs principales del proyecto Alojamientos."""
from django.http import HttpResponse
from django.urls import path, include
from django.contrib import admin
from .views import (
    AlojamientoListView, AlojamientoDetailView,
    AlojamientoCreateView, AlojamientoUpdateView, AlojamientoDeleteView,
    HomeView, DashboardView
)
def home(_request):
    """Vista de inicio del proyecto."""
    return HttpResponse("Bienvenido a Alojamientos")


app_name = 'alojamientos'  # pylint: disable=invalid-name

urlpatterns = [
    path("admin/", admin.site.urls),
    path("clientes/", include("clientes.urls")),
    path("cabanas/", include("cabanas.urls")),
    path("alquileres/", include("alquileres.urls")),
    path("", HomeView.as_view(), name="home"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("alojamientos/", AlojamientoListView.as_view(), name="lista_alojamientos"),
    path("alojamientos/<int:pk>/", AlojamientoDetailView.as_view(), name="detalle_alojamiento"),
    path("alojamientos/nuevo/", AlojamientoCreateView.as_view(), name="crear_alojamiento"),
    path("alojamientos/<int:pk>/editar/", AlojamientoUpdateView.as_view(), name="editar_alojamiento"),
    path("alojamientos/<int:pk>/eliminar/", AlojamientoDeleteView.as_view(), name="eliminar_alojamiento"),
]

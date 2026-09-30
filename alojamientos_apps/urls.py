"""
urls.py - Configuración de URLs para la app alojamientos_apps
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_alojamientos, name="lista_alojamientos"),
    path("<int:pk>/", views.AlojamientoDetailView.as_view(), name="detalle_alojamiento"),
    path("nuevo/", views.AlojamientoCreateView.as_view(), name="crear_alojamiento"),
    path("<int:pk>/editar/", views.AlojamientoUpdateView.as_view(), name="editar_alojamiento"),
    path("<int:pk>/eliminar/", views.AlojamientoDeleteView.as_view(), name="eliminar_alojamiento"),
]

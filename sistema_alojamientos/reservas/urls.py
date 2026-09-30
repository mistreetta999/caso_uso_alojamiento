"""urls.py - Configuración de URLs de la aplicación de reservas."""
from django.urls import path
from .views import (
    ReservaListView,
    ReservaDetailView,
    ReservaCreateView,
    ReservaUpdateView,
    ReservaDeleteView,
)

app_name = "reservas"

urlpatterns = [
    path("", ReservaListView.as_view(), name="list"),
    path("<int:pk>/", ReservaDetailView.as_view(), name="detail"),
    path("crear/", ReservaCreateView.as_view(), name="create"),
    path("<int:pk>/editar/", ReservaUpdateView.as_view(), name="update"),
    path("<int:pk>/eliminar/", ReservaDeleteView.as_view(), name="delete"),
]

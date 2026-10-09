"""urls.py - Configuración de URLs de la aplicación de reservas."""
from django.urls import path
    # include eliminado (evita bucle)
from . import views



urlpatterns = [
    # Funciones simples
    path("", views.index, name="index"),
    path("lista/", views.lista_reservas, name="lista"),
    path("sistema/", views.SistemaUnificadoView.as_view(), name="sistema_unificado"),

    # Vistas basadas en clases (CRUD)
    path("lista-class/", views.ReservaListView.as_view(), name="lista_reservas_class"),
    path("detalle/<int:pk>/", views.ReservaDetailView.as_view(), name="detalle_reserva"),
    path("crear/", views.ReservaCreateView.as_view(), name="crear_reserva"),
    path("editar/<int:pk>/", views.ReservaUpdateView.as_view(), name="editar_reserva"),
    path("eliminar/<int:pk>/", views.ReservaDeleteView.as_view(), name="eliminar_reserva"),
]
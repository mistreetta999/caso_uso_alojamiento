from django.urls import path
from . import views

urlpatterns = [
    # Funciones simples
    path("", views.lista_cabanas, name="lista_cabanas"),
    path("vistas/", views.lista_cabanas_vistas, name="lista_cabanas_vistas"),
    path("alojamientos/", views.lista_alojamientos, name="lista_alojamientos"),
    path("index/", views.index, name="cabanas_index"),

    # Vistas basadas en clases
    path("inicio/", views.InicioView.as_view(), name="cabanas_inicio"),
    path("sistema/", views.SistemaUnificadoView.as_view(), name="cabanas_sistema_unificado"),
]

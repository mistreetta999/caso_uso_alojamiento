from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("alojamientos/", views.lista_alojamientos, name="lista_alojamientos"),
    path("alojamiento/<int:alojamiento_id>/", views.detalle_alojamiento, name="detalle_alojamiento"),
]

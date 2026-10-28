# urls.py (idéntico en clientes_app, reservas_app, cabanas_app, alojamientos_app)

from django.urls import path

from . import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("<str:modelo>/", views.listar, name="listar"),
    path("<str:modelo>/nuevo/", views.crear, name="crear"),
    path("<str:modelo>/<int:pk>/editar/", views.editar, name="editar"),
    path("<str:modelo>/<int:pk>/eliminar/", views.eliminar, name="eliminar"),
]
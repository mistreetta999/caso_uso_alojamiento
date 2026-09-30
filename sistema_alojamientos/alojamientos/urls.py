""" urls.py - Configuración de URLs del proyecto de alojamientos. """
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "alojamientos"  # pylint: disable=invalid-name

urlpatterns = [
    path("", views.AlojamientoListView.as_view(), name="list"),
    path("<int:pk>/", views.AlojamientoDetailView.as_view(), name="detail"),
    path("crear/", views.AlojamientoCreateView.as_view(), name="create"),
    path("<int:pk>/editar/", views.AlojamientoUpdateView.as_view(), name="update"),
    path("<int:pk>/eliminar/", views.AlojamientoDeleteView.as_view(), name="delete"),

    path("admin/", admin.site.urls),  # ✅ admin directo
    path("alojamientos/", include(("alojamientos_app.urls", "alojamientos_app"), namespace="alojamientos_app")),
    path("clientes/", include(("clientes.urls", "clientes"), namespace="clientes")),
    path("reservas/", include(("reservas.urls", "reservas"), namespace="reservas")),
    path("cabanas/", include(("cabanas.urls", "cabanas"), namespace="cabanas")),
]


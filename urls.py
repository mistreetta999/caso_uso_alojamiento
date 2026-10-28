from django.contrib import admin
from django.urls import include, path

from sistemas_alojamiento_app import views


urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),

    path(
        "sistema-unificado/",
        views.SistemaUnificadoView.as_view(),
        name="sistema_unificado",
    ),

    path(
        "dashboard/",
        views.DashboardView.as_view(),
        name="dashboard",
    ),

    path(
        "alojamientos/",
        include(
            "sistemas_alojamiento_app.alojamientos_app.urls"
        ),
    ),

    path(
        "cabanas/",
        include(
            "sistemas_alojamiento_app.cabanas_app.urls"
        ),
    ),

    path(
        "clientes/",
        include(
            "sistemas_alojamiento_app.clientes_app.urls"
        ),
    ),

    path(
        "reservas/",
        include(
            "sistemas_alojamiento_app.reservas_app.urls"
        ),
    ),
]

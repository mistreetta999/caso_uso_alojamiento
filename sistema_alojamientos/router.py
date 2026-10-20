from django.urls import include, path

urlpatterns = [
    path("clientes/", include("clientes.urls")),
    path("reservas/", include("reservas.urls")),
    path("cabanas/", include("cabanas.urls")),
    path("alojamientos/", include("alojamientos.urls")),

    # Si también usás las apps con sufijo _app
    path("clientes_app/", include("clientes_app.urls")),
    path("reservas_app/", include("reservas_app.urls")),
    path("cabanas_app/", include("cabanas_app.urls")),
    path("alojamientos_app/", include("alojamientos_app.urls")),
]

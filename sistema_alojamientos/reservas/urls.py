"""URLs de la aplicación de reservas."""
from django.urls import path
from . import views
from django.urls import include
app_name = "reservas"

urlpatterns = [
    # CRUD con vistas genéricas
    path("", views.ReservaListView.as_view(), name="list"),
    path("<int:pk>/", views.ReservaDetailView.as_view(), name="detail"),
    path("nueva/", views.ReservaCreateView.as_view(), name="create"),
    path("<int:pk>/editar/", views.ReservaUpdateView.as_view(), name="update"),
    path("<int:pk>/eliminar/", views.ReservaDeleteView.as_view(), name="delete"),
    path ("clientes/",include("clientes_app.urls")),
    # Vistas simples adicionales
    path("respuesta/", views.respuesta_root, name="respuesta_root"),
    path("sistema/", views.sistema_unificado, name="sistema_unificado"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("index/", views.index, name="index"),
    path("lista/", views.lista_reservas, name="lista_reservas"),
]

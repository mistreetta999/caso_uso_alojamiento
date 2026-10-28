"""URLs de la aplicación de reservas."""
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from . import views
from django.urls import include
from .views import (
    ClienteViewSet,
    ReservaViewSet,
    crear_reserva,
    dashboard,
    index,
    lista_reservas,
    reservas_app_view,
    sistema_unificado,
)
router = DefaultRouter()
app_name = "reservas"

router = DefaultRouter()

router.register(r"clientes", ClienteViewSet, basename="cliente")
router.register(r"reservas", ReservaViewSet, basename="reserva")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # Ruta raíz principal (tu panel con las tarjetas)
    path('', TemplateView.as_view(template_name='sistema_alojamiento/sistema_unificado.html'), name='sistema_unificado'),

    # Rutas que abren cada una de tus aplicaciones
    path('clientes/', include('sistemas_alojamiento_app.clientes_app.urls')),
    path('reservas/', include('sistemas_alojamiento_app.reservas_app.urls')),
    path('cabanas/', include('sistemas_alojamiento_app.cabanas_app.urls')),
    path('alojamientos/', include('sistemas_alojamiento_app.alojamientos_app.urls')),

    # CRUD con vista
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
        path("", reservas_app_view, name="reservas_app"),
    path("sistema/", sistema_unificado, name="sistema_unificado"),
    path("dashboard/", dashboard, name="dashboard"),
    path("inicio/", index, name="index"),
    path("lista/", lista_reservas, name="lista_reservas"),
    path("crear/", crear_reserva, name="crear_reserva"),
    path("api/", include(router.urls)),
]



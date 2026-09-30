""" urls.py - Configuración de URLs del proyecto de alojamientos. """
from django.contrib import admin
from django.urls import path
import views

urlpatterns = [
    # Admin de Django
    path("admin/", admin.site.urls),

    # Página de inicio
    path("", views.home, name="home"),

    # Vistas individuales por app
    path("cabanas/", views.lista_cabanas, name="lista_cabanas"),
    path("clientes/", views.lista_clientes, name="lista_clientes"),
    path("reservas/", views.lista_reservas, name="lista_reservas"),
    path("alojamientos/", views.lista_alojamientos, name="lista_alojamientos"),
   
    # Vista unificada con todo el sistema
    path("sistema/", views.sistema_unificado, name="sistema_unificado"),

    # Vistas genéricas basadas en clases para alojamientos
    path("alojamientos/lista/", views.AlojamientoListView.as_view(), name="lista_alojamientos"),
    path("alojamientos/<int:pk>/", views.AlojamientoDetailView.as_view(), name="detalle_alojamiento"),
    path("alojamientos/nuevo/", views.AlojamientoCreateView.as_view(), name="crear_alojamiento"),
    path("alojamientos/<int:pk>/editar/", views.AlojamientoUpdateView.as_view(), name="editar_alojamiento"),
    path("alojamientos/<int:pk>/eliminar/", views.AlojamientoDeleteView.as_view(), name="eliminar_alojamiento"),

    # Dashboard opcional
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
]



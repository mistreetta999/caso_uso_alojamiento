from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Apuntando al nombre real de las carpetas de tus apps:
    path('clientes/', include(('clientes_app.urls', 'clientes'), namespace='clientes')),
    path('reservas/', include(('reservas_app.urls', 'reservas'), namespace='reservas')),
    path('cabanas/', include(('cabanas_app.urls', 'cabanas'), namespace='cabanas')),
    path('alojamientos/', include(('alojamientos_app.urls', 'alojamientos'), namespace='alojamientos')),

    # Tus vistas principales...
    path("", views.sistema_unificado, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("inicio/", views.inicio, name="inicio"),
    path("ayuda/", views.AyudaView.as_view(), name="ayuda"),
    path("contacto/", views.ContactoView.as_view(), name="contacto"),
    path("sistema/", views.SistemaUnificadoView.as_view(), name="sistema_unificado"),
    path("nueva/", views.crear_reserva, name="crear_reserva"),
    path("respuesta/", views.respuesta_root, name="respuesta_root"),
]
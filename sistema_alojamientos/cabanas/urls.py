from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

app_name = "cabanas"  # pylint: disable=invalid-name
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
    path("", views.lista_cabanas, name="lista_cabanas"),
    path("vistas/", views.lista_cabanas_vistas, name="lista_cabanas_vistas"),
    path("alojamientos/", views.lista_alojamientos, name="lista_alojamientos"),
    path("index/", views.index, name="cabanas_index"),

    # Vistas basadas en clases
    path("inicio/", views.InicioView.as_view(), name="cabanas_inicio"),
    path("sistema/", views.SistemaUnificadoView.as_view(), name="cabanas_sistema_unificado"),
]


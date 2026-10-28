from django.core import paginator
from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.contrib import admin
from django.urls import include
from clientes .views import SistemaUnificadoView
from .views import ClienteCreateView, ClienteDetailView, listar_clientes    

app_name = "clientes" 

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

    path('admin/', admin.site.urls),
    path("list/", views.ClienteListView.as_view(), name="list"),

    path('clientes_app/', include('clientes_app.urls')),
    path("", views.index, name="clientes_home"),
    path("", views.index, name="index"),                         # Página principal
    path("sistema/", views.SistemaUnificadoView.as_view(), name="sistema"),
    path("listar/", views.listar_clientes, name="listar"),       # Función simple
    path("list/", views.ClienteListView.as_view(), name="list"), # ListView genérica
    path("crear/", views.ClienteCreateView.as_view(), name="crear"),
    path("<int:pk>/detalle/", views.ClienteDetailView.as_view(), name="detalle"),
]



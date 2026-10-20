from django.core import paginator
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include
from .views import SistemaUnificadoView
from .views import ClienteCreateView, ClienteDetailView, listar_clientes    

app_name = "clientes" 

urlpatterns = [
    #
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


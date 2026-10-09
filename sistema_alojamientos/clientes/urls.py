from django.urls import path
from . import views

app_name = "clientes"

urlpatterns = [
    path("", views.index, name="index"),                         # Página principal
    path("sistema/", views.SistemaUnificadoView.as_view(), name="sistema"),
    path("listar/", views.listar_clientes, name="listar"),       # Función simple
    path("list/", views.ClienteListView.as_view(), name="list"), # ListView genérica
    path("crear/", views.ClienteCreateView.as_view(), name="crear"),
    path("<int:pk>/detalle/", views.ClienteDetailView.as_view(), name="detalle"),
]


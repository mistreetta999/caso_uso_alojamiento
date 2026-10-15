from django.urls import path
from .views import IndexView, CabanaListView, CabanaDetailView, CabanaCreateView, CabanaUpdateView

from . import views

app_name = "cabanas"
urlpatterns = [
    path("", views.index, name="index"),
    path("", views.home, name="home"),
    path("nueva/", views.nueva, name="nueva"),
    path("<int:cabana_id>/", views.detalle, name="detalle"),
    path("<int:cabana_id>/editar/", views.editar, name="editar"),
    path("", IndexView.as_view(), name="index"),
    path("listar/", CabanaListView.as_view(), name="listar_cabanas"),
    path("<int:pk>/", CabanaDetailView.as_view(), name="detalle_cabana"),
    path("crear/", CabanaCreateView.as_view(), name="crear_cabana"),
    path("editar/<int:pk>/", CabanaUpdateView.as_view(), name="editar_cabana"),
]

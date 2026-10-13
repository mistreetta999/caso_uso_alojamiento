from django.urls import path
from .views import IndexView, CabanaListView, CabanaDetailView, CabanaCreateView, CabanaUpdateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("listar/", CabanaListView.as_view(), name="listar_cabanas"),
    path("<int:pk>/", CabanaDetailView.as_view(), name="detalle_cabana"),
    path("crear/", CabanaCreateView.as_view(), name="crear_cabana"),
    path("editar/<int:pk>/", CabanaUpdateView.as_view(), name="editar_cabana"),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CabanaViewSet, CabanaListView, CabanaDetailView, CabanaCreateView, CabanaUpdateView, CabanaDeleteView
from . import views

app_name = "cabanas_app"

router = DefaultRouter()
router.register(r"cabanas", CabanaViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("", views.lista_cabanas, name="lista_cabanas"),
    path("<int:id>/", views.detalle_cabana, name="detalle_cabana"),
    path("listar/", CabanaListView.as_view(), name="listar_cabanas"),
    path("<int:pk>/detalle/", CabanaDetailView.as_view(), name="detalle_cabana"),
    path("crear/", CabanaCreateView.as_view(), name="crear_cabana"),
    path("<int:pk>/editar/", CabanaUpdateView.as_view(), name="editar_cabana"),
    path("<int:pk>/eliminar/", CabanaDeleteView.as_view(), name="eliminar_cabana"),
    path("", views.index, name="index"),
    path("", views.CabanaListView.as_view(), name="index"),
    path("<int:pk>/", views.CabanaDetailView.as_view(), name="detalle"),
    path("nuevo/", views.CabanaCreateView.as_view(), name="nuevo"),
    path("actualizar/<int:pk>/", views.CabanaUpdateView.as_view(), name="actualizar"),
    path("eliminar/<int:pk>/", views.CabanaDeleteView.as_view(), name="eliminar"),
]
urlpatterns = router.urls

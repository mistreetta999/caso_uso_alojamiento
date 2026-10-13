from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cabanas_app.views import (
    IndexView, CabanaListView, CabanaDetailView,
    CabanaCreateView, CabanaUpdateView, CabanaViewSet
)

# Router para la API REST
router = DefaultRouter()
router.register(r'api/cabanas', CabanaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Vistas HTML
    path("cabanas/", CabanaListView.as_view(), name="listar_cabanas"),
    path("cabanas/<int:pk>/", CabanaDetailView.as_view(), name="detalle_cabana"),
    path("cabanas/crear/", CabanaCreateView.as_view(), name="crear_cabana"),
    path("cabanas/editar/<int:pk>/", CabanaUpdateView.as_view(), name="editar_cabana"),
    path("", IndexView.as_view(), name="index"),

    # API REST
    path("", include(router.urls)),
]

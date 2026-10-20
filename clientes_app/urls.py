"""URLs for the clientes_app."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet
from . import views

# Router exclusivo para la API de clientes
router = DefaultRouter()
router.register(r'', ClienteViewSet, basename='cliente-api')

app_name = 'clientes'

urlpatterns = [
    # Rutas de la API
    path('api/', include(router.urls)),
    # Rutas tradicionales (HTML) - Llamadas como funciones directas sin .as_view()
    path("lista/", views.ClienteListView.as_view(), name="lista"),
    path("create/", views.ClienteCreateView.as_view(), name="create"),
    path("update/<int:pk>/", views.ClienteUpdateView, name="update"),
    path("delete/<int:pk>/", views.ClienteDeleteView, name="delete"),
]
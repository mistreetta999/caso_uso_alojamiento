"""URLs para la aplicación de alquileres."""
from django.urls import path
from .views import AlquilerListView, AlquilerCreateView, AlquilerDetailView

app_name = "alquileres"  # pylint: disable=invalid-name

urlpatterns = [
    path("", AlquilerListView.as_view(), name="list"),
    path("nuevo/", AlquilerCreateView.as_view(), name="create"),
    path("<int:pk>/", AlquilerDetailView.as_view(), name="detail"),
]

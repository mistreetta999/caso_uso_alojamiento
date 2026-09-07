"""
URLs for the 'clientes' app.
"""
from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteDetailView

app_name = "clientes"  # pylint: disable=invalid-name

urlpatterns = [
    path("", ClienteListView.as_view(), name="list"),
    path("nuevo/", ClienteCreateView.as_view(), name="create"),
    path("<int:pk>/", ClienteDetailView.as_view(), name="detail"),
]

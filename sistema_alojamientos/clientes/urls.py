"""
URLs for the 'clientes' app.
"""
from django.urls import path
from .views import HomeView, ClienteListView, ClienteCreateView, ClienteDetailView

app_name = "clientes"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("lista/", ClienteListView.as_view(), name="list"),
    path("nuevo/", ClienteCreateView.as_view(), name="create"),
    path("detalle/<int:pk>/", ClienteDetailView.as_view(), name="detail"),
]

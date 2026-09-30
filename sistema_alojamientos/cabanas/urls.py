"""URLs de la aplicación Cabañas."""
from django.urls import path
from django.urls import include
from .views import (
    CabanaDetailView,
    CabanaCreateView,
    CabanaUpdateView,
    CabanaDeleteView
)

app_name = 'cabanas'  # pylint: disable=invalid-name

urlpatterns = [
    
    path('<int:pk>/', CabanaDetailView.as_view(), name='cabana_detail'),
    path('nueva/', CabanaCreateView.as_view(), name='cabana_create'),
    path('<int:pk>/editar/', CabanaUpdateView.as_view(), name='cabana_edit'),
    path('<int:pk>/eliminar/', CabanaDeleteView.as_view(), name='cabana_delete'),
    path('alojamientos/', include(('alojamientos_apps.urls', 'alojamientos'), namespace='alojamientos')),
    
]

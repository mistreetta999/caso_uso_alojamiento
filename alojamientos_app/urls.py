from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import ClienteViewSet
from . import views
app_name = 'alojamientos'

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('clientes_app.urls')),
    # Vistas clásicas
    path("", views.index, name="index_alojamientos"),
    path("lista/", views.AlojamientoListView.as_view(), name="lista"),
    
    path('', views.lista_alojamientos, name='lista_alojamientos'),
    path("crear/", views.crear_alojamiento, name="crear_alojamiento"),  # cspell:ignore crear
    path("dashboard/", views.dashboard, name="dashboard_alojamientos"),

    # Vistas con TemplateView
    path("inicio/", views.InicioView.as_view(), name="inicio"),
    path("sistema_unificado/", views.SistemaUnificadoView.as_view(), name="sistema_unificado"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("dashboard_view/", views.DashboardView.as_view(), name="dashboard_view"),

    # CRUD con genéricos
    path("list/", views.AlojamientoListView.as_view(), name="alojamiento_list"),
    path("<int:pk>/detalle/", views.AlojamientoDetailView.as_view(), name="alojamiento_detail"),
    path("nuevo/", views.AlojamientoCreateView.as_view(), name="alojamiento_create"),
    path("<int:pk>/editar/", views.AlojamientoUpdateView.as_view(), name="alojamiento_update"),
    path("<int:pk>/eliminar/", views.AlojamientoDeleteView.as_view(), name="alojamiento_delete"),
]
urlpatterns = router.urls

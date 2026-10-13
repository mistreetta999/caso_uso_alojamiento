from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from alojamientos_app.views import AlojamientoViewSet
from clientes_app.views import ClienteViewSet
from cabanas_app.views import CabanaViewSet
from reservas_app.views import ReservaViewSet


from . import views

router = routers.DefaultRouter()
router.register(r"clientes", ClienteViewSet)
router.register(r"alojamientos", AlojamientoViewSet)
router.register(r"cabanas", CabanaViewSet)
router.register(r"reservas", ReservaViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
    # Funciones simples
    path("", views.lista_alojamientos, name="lista_alojamientos"),
    path("index/", views.index, name="alojamientos_index"),
    path("dashboard/", views.dashboard, name="alojamientos_dashboard"),

    # Vistas basadas en clases
    path("inicio/", views.InicioView.as_view(), name="inicio"),
    path("sistema/", views.SistemaUnificadoView.as_view(), name="sistema_unificado"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("panel/", views.DashboardView.as_view(), name="dashboard_view"),

    # CRUD de alojamientos con vistas genéricas
    path("lista/", views.AlojamientoListView.as_view(), name="lista_alojamientos_class"),
    path("detalle/<int:pk>/", views.AlojamientoDetailView.as_view(), name="detalle_alojamiento"),
    path("crear/", views.AlojamientoCreateView.as_view(), name="crear_alojamiento"),
    path("editar/<int:pk>/", views.AlojamientoUpdateView.as_view(), name="editar_alojamiento"),
    path("eliminar/<int:pk>/", views.AlojamientoDeleteView.as_view(), name="eliminar_alojamiento"),
] 
urlpatterns += router.urls

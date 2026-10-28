from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.views.generic import TemplateView
from alojamientos_app.views import AlojamientoViewSet
from clientes_app.views import ClienteViewSet
from sistemas_alojamiento_app.cabanas_app.views import CabanaViewSet
from sistemas_alojamiento_app.reservas_app.views import ReservaViewSet
from django.contrib import admin
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r"clientes", ClienteViewSet)
router.register(r"alojamientos", AlojamientoViewSet)
router.register(r"cabanas", CabanaViewSet)
router.register(r"reservas", ReservaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
    "sistema-unificado/",
    views.SistemaUnificadoView.as_view(),
    name="sistema_unificado",
),
    # Ruta raíz principal (tu panel con las tarjetas)
    path('', TemplateView.as_view(template_name='sistema_alojamiento/sistema_unificado.html'), name='sistema_unificado'),

    # Rutas que abren cada una de tus aplicaciones
    path('clientes/', include('sistemas_alojamiento_app.clientes_app.urls')),
    path('reservas/', include('sistemas_alojamiento_app.reservas_app.urls')),
    path('cabanas/', include('sistemas_alojamiento_app.cabanas_app.urls')),
    path('alojamientos/', include('sistemas_alojamiento_app.alojamientos_app.urls')),

    #ruta template django
    path('alojamiento/',TemplateView.as_view(template_name="alojamiento_list.html"),
    path('alojamiento/',TemplateView.as_view(template_name="alojamiento.html"),
    path('alojamiento/',TemplateView.as_view(template_name="desabord.html"),
    path('alojamiento/',TemplateView.as_view(template_name="global.html"),
    path('alojamiento/',TemplateView.as_view(template_name="base.html"),
    path('alojamiento/',TemplateView.as_view(template_name="bootstrap.html"),
    path('alojamiento/',TemplateView.as_view(template_name="lista_alojamiento.html"),
    #ruta template app
    path('alojamiento_app/',TemplateView.as_view(template_name="alojamiento_list.html"),
    path('alojamiento_app/',TemplateView.as_view(template_name="alojamiento.html"),
    path('alojamiento_app/',TemplateView.as_view(template_name="desabord.html"),
    path('alojamiento_app/',TemplateView.as_view(template_name="global.html"),
    path('alojamiento_app/',TemplateView.as_view(template_name="base.html"),
    path('alojamiento_app/',TemplateView.as_view(template_name="bootstrap.html"),
    path('alojamiento_app/',TemplateView.as_view(template_name="lista_alojamiento.html"),
         
         
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
    # Funciones simples
    path("", views.lista_alojamientos, name="lista_alojamientos"),
    path("index/", views.index, name="index"),
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
path('', views.lista_alojamientos, name='lista'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('nuevo/', views.nuevo_alojamiento, name='nuevo'),
    path('detalle/<int:pk>/', views.detalle_alojamiento, name='detalle'),
    path('editar/<int:pk>/', views.editar_alojamiento, name='editar'),
    path('eliminar/<int:pk>/', views.eliminar_alojamiento, name='eliminar'),
    path('sistema_unificado/', views.sistema_unificado, name='sistema_unificado'),
    path('root/', views.respuesta_root, name='respuesta_root'),
]


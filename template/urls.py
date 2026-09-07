"""URLs de la aplicación Template."""
from django.urls import path
from template import views

app_name = "template"  # pylint: disable=invalid-name

urlpatterns = [
    path('', views.TemplateListView.as_view(), name='template_lista'),
    path('nuevo/', views.TemplateCreateView.as_view(), name='template_crear'),
    path('<int:pk>/', views.TemplateDetailView.as_view(), name='template_detalle'),
    path('<int:pk>/editar/', views.TemplateUpdateView.as_view(), name='template_editar'),
    path('<int:pk>/eliminar/', views.TemplateDeleteView.as_view(), name='template_eliminar'),
]

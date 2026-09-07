"""
Vistas de la aplicación de alojamientos.
"""
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse

# Ejemplo de vista Home
class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return HttpResponse("Bienvenido al sistema de alojamientos")

# Ejemplo de Dashboard
class DashboardView(TemplateView):
    template_name = "dashboard.html"


# Si tenés un modelo Alojamiento en alojamientos/models.py
from alojamientos.models import Alojamiento

# Listar alojamientos
class AlojamientoListView(ListView):
    model = Alojamiento
    template_name = "alojamientos/lista_alojamientos.html"
    context_object_name = "alojamientos"

# Detalle de un alojamiento
class AlojamientoDetailView(DetailView):
    model = Alojamiento
    template_name = "alojamientos/detalle_alojamiento.html"
    context_object_name = "alojamiento"

# Crear alojamiento
class AlojamientoCreateView(CreateView):
    model = Alojamiento
    template_name = "alojamientos/form_alojamiento.html"
    fields = ["nombre", "direccion", "capacidad", "precio"]
    success_url = reverse_lazy("lista_alojamientos")

# Editar alojamiento
class AlojamientoUpdateView(UpdateView):
    model = Alojamiento
    template_name = "alojamientos/form_alojamiento.html"
    fields = ["nombre", "direccion", "capacidad", "precio"]
    success_url = reverse_lazy("lista_alojamientos")

# Eliminar alojamiento
class AlojamientoDeleteView(DeleteView):
    model = Alojamiento
    template_name = "alojamientos/confirmar_eliminar.html"
    success_url = reverse_lazy("lista_alojamientos")

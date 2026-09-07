"""Vistas de la aplicación de alojamientos."""
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from alojamientos.models import Alojamiento

class HomeView(TemplateView):
    """Vista de inicio que redirige a alojamientos."""
    def get(self, request, *args, **kwargs):
        return redirect("lista_alojamientos")


# Vista Dashboard
class DashboardView(TemplateView):
    """Vista del panel de control del sistema de alojamientos."""   
    template_name = "dashboard.html"


# Importar el modelo Alojamiento

# Listar alojamientos
class AlojamientoListView(ListView):
    """Vista para listar todos los alojamientos."""
    model = Alojamiento
    template_name = "alojamientos/lista_alojamientos.html"
    context_object_name = "alojamientos"

# Detalle de un alojamiento
class AlojamientoDetailView(DetailView):
    """Vista para mostrar el detalle de un alojamiento específico."""
    model = Alojamiento
    template_name = "alojamientos/detalle_alojamiento.html"
    context_object_name = "alojamiento"

# Crear alojamiento
class AlojamientoCreateView(CreateView):
    """Vista para crear un nuevo alojamiento."""
    model = Alojamiento
    template_name = "alojamientos/form_alojamiento.html"
    fields = ["nombre", "direccion", "capacidad", "precio"]
    success_url = reverse_lazy("lista_alojamientos")

# Editar alojamiento
class AlojamientoUpdateView(UpdateView):
    """Vista para editar un alojamiento existente."""
    model = Alojamiento
    template_name = "alojamientos/form_alojamiento.html"
    fields = ["nombre", "direccion", "capacidad", "precio"]
    success_url = reverse_lazy("lista_alojamientos")

# Eliminar alojamiento
class AlojamientoDeleteView(DeleteView):
    """Vista para eliminar un alojamiento existente."""
    model = Alojamiento
    template_name = "alojamientos/confirmar_eliminar.html"
    success_url = reverse_lazy("lista_alojamientos")

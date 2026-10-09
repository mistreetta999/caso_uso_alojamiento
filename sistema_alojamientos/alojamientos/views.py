"""Vistas de la aplicación de alojamientos."""
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from ..cabanas.models import Cabana
from .models import Alojamiento

def cabanas(request):
    """Vista para listar todas las cabañas."""
    cabanas = Cabana.objects.all()
    return render(request, "cabanas/lista.html", {"cabanas": cabanas})
def lista_alojamientos(request):
    """Vista para listar alojamientos con función simple."""
    alojamientos = Alojamiento._default_manager.all()  # pylint: disable=protected-access
    return render(request, "alojamientos/index.html", {"alojamientos": alojamientos})
def index(request):
    """Muestra la página principal de alojamientos."""
    return HttpResponse("Página de alojamientos")

# Vista de inicio
class InicioView(TemplateView):
    """Vista de inicio del sistema de alojamientos."""
    template_name = "inicio.html"


# Vista principal del sistema unificado
class SistemaUnificadoView(TemplateView):
    """Vista principal del sistema unificado."""
    template_name = "sistema_unificado.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["alojamientos"] = Alojamiento._default_manager.all()  # pylint: disable=protected-access
        return contexto

def lista_alojamientos(request):
    """Vista para listar alojamientos con función simple."""
    alojamientos = Alojamiento._default_manager.all()  # pylint: disable=protected-access
    return render(request, "alojamientos/index.html", {"alojamientos": alojamientos})


def dashboard(request):
    """Vista para mostrar el panel de control del sistema de alojamientos."""
    return render(request, "alojamientos/dashboard.html")


class HomeView(TemplateView):
    """Vista de inicio que redirige a alojamientos."""
    def get(self, request, *args, **kwargs):
        return redirect("lista_alojamientos")


class DashboardView(TemplateView):
    """Vista del panel de control del sistema de alojamientos."""   
    template_name = "alojamientos/dashboard.html"


class AlojamientoListView(ListView):
    """Vista para listar todos los alojamientos."""
    model = Alojamiento
    template_name = "alojamientos/lista_alojamientos.html"
    context_object_name = "alojamientos"


class AlojamientoDetailView(DetailView):
    """Vista para mostrar el detalle de un alojamiento específico."""
    model = Alojamiento
    template_name = "alojamientos/detalle_alojamiento.html"
    context_object_name = "alojamiento"


class AlojamientoCreateView(CreateView):
    """Vista para crear un nuevo alojamiento."""
    model = Alojamiento
    template_name = "alojamientos/form_alojamiento.html"
    fields = ["nombre", "direccion", "capacidad", "precio"]
    success_url = reverse_lazy("lista_alojamientos")


class AlojamientoUpdateView(UpdateView):
    """Vista para editar un alojamiento existente."""
    model = Alojamiento
    template_name = "alojamientos/form_alojamiento.html"
    fields = ["nombre", "direccion", "capacidad", "precio"]
    success_url = reverse_lazy("lista_alojamientos")


class AlojamientoDeleteView(DeleteView):
    """Vista para eliminar un alojamiento existente."""
    model = Alojamiento
    template_name = "alojamientos/confirmar_eliminar.html"
    success_url = reverse_lazy("lista_alojamientos")

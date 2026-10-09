"""
Vistas del módulo de alojamientos.
"""
from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from sistema_alojamientos.cabanas.models import Cabana
from sistema_alojamientos.clientes.models import Cliente
from sistema_alojamientos.reservas.models import Reserva
from sistema_alojamientos.alojamientos.models import Alojamiento

class InicioView(TemplateView):  # pylint: disable=too-few-public-methods
    """Vista de inicio del módulo de alojamientos."""
    template_name = "inicio.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mensaje"] = "Bienvenido al módulo de alojamientos"
        return context


# Vista de inicio (función simple)
def inicio(request):
    return render(request, "inicio.html")

# Vista unificada (Class-Based View)
class SistemaUnificadoView(View):
    """Vista unificada que muestra cabanas, clientes, reservas y alojamientos."""
    def get(self, request):
        contexto = {
            "cabanas": Cabana.objects.all(),
            "clientes": Cliente.objects.all(),
            "reservas": Reserva.objects.select_related("cliente", "cabana").all(),
            "alojamientos": Alojamiento.objects.all(),
        }
        return render(request, "sistema_unificado.html", contexto)

def index(request):
    """Vista de índice del módulo de alojamientos."""
    return HttpResponse("Bienvenido al módulo de alojamientos")

def lista_alojamientos(request):
    """Vista de la lista de alojamientos del módulo de alojamientos."""
    alojamientos = Alojamiento.objects.all()  # pylint: disable=no-member
    return render(request, "lista_alojamientos.html", {"alojamientos": alojamientos})

def detalle_alojamiento(request, alojamiento_id):
    """Vista del detalle de un alojamiento del módulo de alojamientos."""
    alojamiento = Alojamiento.objects.get(id=alojamiento_id)  # pylint: disable=no-member
    return render(request, "detalle_alojamiento.html", {"alojamiento": alojamiento})

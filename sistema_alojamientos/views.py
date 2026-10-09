from django.shortcuts import render
from django.views import View
from sistema_alojamientos.cabanas.models import Cabana
from sistema_alojamientos.clientes.models import Cliente
from sistema_alojamientos.reservas.models import Reserva
from sistema_alojamientos.alojamientos.models import Alojamiento
from django.http import HttpResponse
    
def index(request):
    contexto = {
        "cabanas": Cabana.objects.all(),
        "clientes": Cliente.objects.all(),
        "reservas": Reserva.objects.select_related("cliente", "cabana").all(),
        "alojamientos": Alojamiento.objects.all(),
    }
    return render(request, "index.html", contexto)


# Vista de inicio general
class InicioView(View):
    def get(self, request):
        return render(request, "inicio.html")

# Vista unificada que conecta todas las apps
class SistemaUnificadoView(View):
    """Vista que muestra un sistema unificado con información de todas las apps."""
    def get(self, request):
        contexto = {
            "cabanas": Cabana.objects.all(),
            "clientes": Cliente.objects.all(),
            "reservas": Reserva.objects.select_related("cliente", "cabana").all(),
            "alojamientos": Alojamiento.objects.all(),
        }
        return render(request, "sistema_unificado.html", contexto)

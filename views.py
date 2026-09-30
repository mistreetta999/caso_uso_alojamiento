"""
Vistas principales del sistema de alojamientos.
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Importar modelos de cada app
from sistema_alojamientos.cabanas.models import Cabana
from sistema_alojamientos.clientes.models import Cliente
from sistema_alojamientos.reservas.models import Reserva
from sistema_alojamientos.alojamientos.models import Alojamiento
from alojamientos_apps.models import Alojamientos

# Página de inicio
def home(request):
    return render(request, "home.html")

# Listados individuales
def lista_cabanas(request):
    cabanas = Cabana.objects.all()
    return render(request, "cabanas/lista.html", {"cabanas": cabanas})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "clientes/lista.html", {"clientes": clientes})

def lista_reservas(request):
    reservas = Reserva.objects.select_related("cliente", "cabana").all()
    return render(request, "reservas/lista.html", {"reservas": reservas})

def lista_alojamientos(request):
    alojamientos = Alojamientos.objects.all()
    return render(request, "alojamientos/lista.html", {"alojamientos": alojamientos})

# Vista unificada
def sistema_unificado(request):
    contexto = {
        "cabanas": Cabana.objects.all(),
        "clientes": Cliente.objects.all(),
        "reservas": Reserva.objects.select_related("cliente", "cabana").all(),
        "alojamientos": Alojamientos.objects.all(),
    }
    return render(request, "sistema_unificado.html", contexto)

# Vistas genéricas basadas en clases
class HomeView(TemplateView):
    template_name = "home.html"
    def get(self, request, *args, **kwargs):
        return HttpResponse("Bienvenido al sistema de alojamientos")

class DashboardView(TemplateView):
    template_name = "dashboard.html"

class AlojamientoListView(ListView):
    model = Alojamiento
    template_name = "alojamientos/lista_alojamientos.html"
    context_object_name = "alojamientos"

class AlojamientoDetailView(DetailView):
    model = Alojamiento
    template_name = "alojamientos/detalle_alojamiento.html"
    context_object_name = "alojamiento"

class AlojamientoCreateView(CreateView):
    model = Alojamiento
    template_name = "alojamientos/form_alojamiento.html"
    fields = ["nombre", "direccion", "capacidad", "precio"]
    success_url = reverse_lazy("lista_alojamientos")

class AlojamientoUpdateView(UpdateView):
    model = Alojamiento
    template_name = "alojamientos/form_alojamiento.html"
    fields = ["nombre", "direccion", "capacidad", "precio"]
    success_url = reverse_lazy("lista_alojamientos")

class AlojamientoDeleteView(DeleteView):
    model = Alojamiento
    template_name = "alojamientos/confirmar_eliminar.html"
    success_url = reverse_lazy("lista_alojamientos")

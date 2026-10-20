"""Vistas de la aplicación de reservas."""
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from reservas_app.models import Reserva


def respuesta_root(request):
    """ ruta respuesta"""
    return render(request, "respuesta_root.html")


def sistema_unificado(request):
    return render(request, "sistema_unificado.html")

def dashboard(request):
    return render(request, "dashboard.html")

class SistemaUnificadoView(View):
    def get(self, request):
        # lógica
        return HttpResponse("Sistema Unificado")

def index(request): # pylint: disable=unused-argument
    """Vista para la página principal de reservas."""
    return HttpResponse(" reservas")

def lista_reservas(request):
    """Vista para listar todas las reservas."""
    reservas = Reserva._default_manager.all()
    return render(request, "reservas/lista_reservas.html", {"reservas": reservas})

class ReservaListView(ListView):
    """Vista para listar todas las reservas."""
    model = Reserva
    template_name = "reservas/reserva_list.html"
    context_object_name = "reservas"


class ReservaDetailView(DetailView):
    """Vista para mostrar los detalles de una reserva."""
    model = Reserva
    template_name = "reservas/reserva_detail.html"
    context_object_name = "reserva"


class ReservaCreateView(CreateView):
    """Vista para crear una nueva reserva."""
    model = Reserva
    fields = ["cliente", "cabana", "fecha_ingreso", "fecha_salida", "observaciones"]
    template_name = "reservas/reserva_form.html"
    success_url = reverse_lazy("reservas:list")


class ReservaUpdateView(UpdateView):
    """Vista para actualizar una reserva existente."""
    model = Reserva
    fields = ["cliente", "cabana", "fecha_ingreso", "fecha_salida", "observaciones"]
    template_name = "reservas/reserva_form.html"
    success_url = reverse_lazy("reservas:list")


class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = "reservas/reserva_confirm_delete.html"
    success_url = reverse_lazy("reservas:list")

"""Vistas de la aplicación de reservas."""
from os import path
from django.http import HttpResponse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Reserva

from django.views import View

class SistemaUnificadoView(View):
    def get(self, request):
        # lógica
        return HttpResponse("Sistema Unificado")

def index(request):
    """Vista para la página principal de reservas."""
    return HttpResponse(" reservas")

def lista_reservas(request):
    """Vista para listar todas las reservas."""
    reservas = Reserva.objects.all()
    return HttpResponse(", ".join([str(reserva) for reserva in reservas]))

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
    """Vista para eliminar una reserva."""
    model = Reserva
    template_name = "reservas/reserva_confirm_delete.html"
    success_url = reverse_lazy("reservas:list")

"""Vistas de la aplicación de reservas."""
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Reserva


class ReservaListView(ListView):
    model = Reserva
    template_name = "reservas/reserva_list.html"
    context_object_name = "reservas"


class ReservaDetailView(DetailView):
    model = Reserva
    template_name = "reservas/reserva_detail.html"
    context_object_name = "reserva"


class ReservaCreateView(CreateView):
    model = Reserva
    fields = ["cliente", "cabana", "fecha_ingreso", "fecha_salida", "observaciones"]
    template_name = "reservas/reserva_form.html"
    success_url = reverse_lazy("reservas:list")


class ReservaUpdateView(UpdateView):
    model = Reserva
    fields = ["cliente", "cabana", "fecha_ingreso", "fecha_salida", "observaciones"]
    template_name = "reservas/reserva_form.html"
    success_url = reverse_lazy("reservas:list")


class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = "reservas/reserva_confirm_delete.html"
    success_url = reverse_lazy("reservas:list")

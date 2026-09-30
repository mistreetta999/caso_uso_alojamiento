"""
views.py - Vistas para la app alojamientos_apps
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Alojamiento
from .forms import AlojamientoForm

# Vista de inicio simple
def home(request):
    return HttpResponse("Bienvenido a la app de alojamientos")

# Listar alojamientos
def lista_alojamientos(request):
    alojamientos = Alojamiento.objects.all()
    return render(request, "alojamientos_apps/lista.html", {"alojamientos": alojamientos})

# CRUD con vistas genéricas
class AlojamientoListView(ListView):
    model = Alojamiento
    template_name = "alojamientos_apps/lista.html"
    context_object_name = "alojamientos"

class AlojamientoDetailView(DetailView):
    model = Alojamiento
    template_name = "alojamientos_apps/detalle.html"
    context_object_name = "alojamiento"

class AlojamientoCreateView(CreateView):
    model = Alojamiento
    form_class = AlojamientoForm
    template_name = "alojamientos_apps/form.html"
    success_url = reverse_lazy("lista_alojamientos")

class AlojamientoUpdateView(UpdateView):
    model = Alojamiento
    form_class = AlojamientoForm
    template_name = "alojamientos_apps/form.html"
    success_url = reverse_lazy("lista_alojamientos")

class AlojamientoDeleteView(DeleteView):
    model = Alojamiento
    template_name = "alojamientos_apps/confirmar_eliminar.html"
    success_url = reverse_lazy("lista_alojamientos")

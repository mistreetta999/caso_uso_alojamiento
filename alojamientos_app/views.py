"""Vistas de la aplicación de alojamientos."""

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets

from clientes_app.models import Cliente
from clientes_app.serializers import ClienteSerializer
from reservas_app.models import Reserva
from reservas_app.serializers import ReservaSerializer

from .models import Alojamiento
from .serializers import AlojamientoSerializer
from .forms import AlojamientoForm


def respuesta_root(request):
    return render(request, "respuesta_root.html")



def sistema_unificado(request: HttpRequest) -> HttpResponse:
    return render(request, "sistema_unificado.html")

def dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, "alojamientos/dashboard.html")
def lista_alojamientos(request: HttpRequest) -> HttpResponse:

    alojamientos = Alojamiento.objects.all()
    return render(request, "alojamientos/index.html", {"alojamientos": alojamientos})
# --- API REST ---
class AlojamientoViewSet(viewsets.ModelViewSet):
    """alojamientos."""
    queryset = Alojamiento.objects.all()
    serializer_class = AlojamientoSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    """API REST para reservas."""
    queryset = Reserva.objects.select_related("cliente").all()
    serializer_class = ReservaSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    """API REST para clientes."""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


# --- Vistas clásicas ---
def index(request):
    return HttpResponse("Alojamientos")


def lista_alojamientos(request):
    alojamientos = Alojamiento.objects.all()
    return render(request, "alojamientos/index.html", {"alojamientos": alojamientos})


def crear_alojamiento(request):
    if request.method == "POST":
        form = AlojamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_alojamientos")
    else:
        form = AlojamientoForm()
    return render(request, "alojamientos/crear_alojamiento.html", {"form": form})


class InicioView(TemplateView):
    template_name = "inicio.html"


class SistemaUnificadoView(TemplateView):
    template_name = "sistema_unificado.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["alojamientos"] = Alojamiento.objects.all()
        return contexto
class AlojamientoListView(TemplateView):
    template_name = "alojamientos/lista_alojamientos.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["alojamientos"] = Alojamiento.objects.all()
        return contexto




class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        return redirect("lista_alojamientos")


class DashboardView(TemplateView):
    template_name = "alojamientos/dashboard.html"


# --- CRUD con genéricos ---
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
    fields = ["nombre", "descripcion", "capacidad", "precio_por_noche"]
    success_url = reverse_lazy("lista_alojamientos")


class AlojamientoUpdateView(UpdateView):
    model = Alojamiento
    template_name = "alojamientos/form_alojamiento.html"
    fields = ["nombre", "descripcion", "capacidad", "precio_por_noche"]
    success_url = reverse_lazy("lista_alojamientos")


class AlojamientoDeleteView(DeleteView):
    model = Alojamiento
    template_name = "alojamientos/confirmar_eliminar.html"
    success_url = reverse_lazy("lista_alojamientos")

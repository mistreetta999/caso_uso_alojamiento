"""Vistas de la aplicación de reservas."""
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from sistemas_alojamiento_app.reservas_app.models import Reserva
from rest_framework import routers
from sistemas_alojamiento_app.reservas_app.views import ReservaViewSet


from django.http import HttpResponse
from django.shortcuts import redirect, render

from rest_framework import viewsets

from cliente_app.models import Cliente
from cliente_app.serializers import ClienteSerializer

from .forms import ReservaForm
from .models import Reserva
from .serializers import ReservaSerializer
router = routers.DefaultRouter()
router.register(r'reservas', ReservaViewSet)

def reservas_app_view(request):
    return render(request, "reservas/reservas.html")


def sistema_unificado(request):
    return render(request, "reservas/global.html")


def dashboard(request):
    return render(request, "reservas/dashboard.html")


def index(request):
    return render(request, "reservas/index.html")


def lista_reservas(request):
    reservas = Reserva.objects.select_related(
        "cliente",
        "cabana",
        "alojamiento",
    ).all()

    return render(
        request,
        "reservas/lista_reservas.html",
        {"reservas": reservas},
    )


def crear_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("sistema_unificado")
    else:
        form = ReservaForm()

    return render(
        request,
        "reservas/crear_reserva.html",
        {"form": form},
    )


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.select_related(
        "cliente",
        "cabana",
        "alojamiento",
    ).all()

    serializer_class = ReservaSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
class ReservaViewSet(request):
    def get(self, request):
        reservas = Reserva.objects.all()
        return render(request, "reservas/lista_reservas.html", {"reservas": reservas})
def respuesta_root(request):
    """ ruta respuesta"""
    return render(request, "respuesta_root.html")


def sistema_unificado(request):
    return render(request, "sistema_unificado.html")

def dashboard(request):
    return render(request, "global/global/dashboard.html")

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


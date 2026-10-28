"""Vistas de la aplicación de alojamientos."""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from .serializers import AlojamientoSerializer, ClienteSerializer, CabanaSerializer, ReservaSerializer      # asegurate de tenerlo

from sistema_alojamientos.alojamientos.models import Alojamiento
from sistema_alojamientos.cabanas.models import Cabana
from sistema_alojamientos.clientes.models import Cliente
from sistema_alojamientos.reservas.models import Reserva
from rest_framework import viewsets
from sistemas_alojamiento_app.reservas_app.models import Reserva

from .serializers import ReservaSerializer
from django.shortcuts import render
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'reservas', ReservaViewSet)
def respuesta_root(request):
    return render(request, "respuesta_root.html")


def sistema_unificado(request):
    return render(request, "sistema_unificado.html")

def dashboard(request):
    return render(request, "global/global/dashboard.html")

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


def index(request):
    return HttpResponse("Alojamientos")

def lista_alojamientos(request):
    alojamientos = Alojamiento.objects.all()
    return render(request, "alojamientos/global/global/index.html", {"alojamientos": alojamientos})


def dashboard(request):
    return render(request, "alojamientos/global/global/dashboard.html")
class InicioView(TemplateView):
    template_name = "inicio.html"

class SistemaUnificadoView(TemplateView):
    template_name = "sistema_unificado.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["alojamientos"] = Alojamiento.objects.all()
        return contexto

class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        return redirect("lista_alojamientos")

class DashboardView(TemplateView):
    template_name = "alojamientos/global/global/dashboard.html"

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
class  ClienteViewSet(viewsets.ModelViewSet):
    """API REST para clientes."""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
class CabanaViewSet(viewsets.ModelViewSet):
    """API REST para cabañas."""
    queryset = Cabana.objects.all()
    serializer_class = CabanaSerializer
class  ReservaViewSet(viewsets.ModelViewSet):
    """API REST para reservas."""
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
class AlojamientoViewSet(viewsets.ModelViewSet):
    """API REST para alojamientos."""
    queryset = Alojamiento.objects.all()
    serializer_class = AlojamientoSerializer


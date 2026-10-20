"""Vistas de la aplicación de clientes."""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from rest_framework import viewsets

from .models import Cliente
from .serializers import ClienteSerializer
from .forms import ClienteForm

from reservas_app.models import Reserva
from reservas_app.serializers import ReservaSerializer
from django.views.generic import CreateView
from .models import Cliente
from django.urls import reverse_lazy

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono'] # Ajusta los campos según tu modelo
    template_name = 'clientes_app/cliente_form.html'
    success_url = reverse_lazy('clientes:lista') # O la ruta de redirección que uses

def index(request):
    """Vista de índice para clientes."""
    return HttpResponse("Clientes")


def cliente_detalles(request, cliente_id):
    """Detalle de un cliente específico."""
    cliente = Cliente.objects.get(id=cliente_id)
    return render(request, "cliente_detalles.html", {"cliente": cliente})


def crear_cliente(request):
    """Formulario para crear un cliente."""
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ClienteForm()
    return render(request, "crear_cliente.html", {"form": form})


def ClienteDeleteView(request, pk):
    """Eliminar un cliente existente."""
    cliente = Cliente.objects.get(pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect("index")
    return render(request, "eliminar_cliente.html", {"cliente": cliente})


def ClienteUpdateView(request, pk):
    """Actualizar datos de un cliente."""
    cliente = Cliente.objects.get(pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ClienteForm(instance=cliente)
    return render(request, "actualizar_cliente.html", {"form": form})


def dashboard(request):
    """Dashboard de clientes (ejemplo con cliente id=1)."""
    cliente = Cliente.objects.get(id=1)
    return render(request, "dashboard.html", {"cliente": cliente})


def respuesta_root(request):
    """Vista raíz de respuesta."""
    return render(request, "respuesta_root.html")


def sistema_unificado(request):
    """Vista del sistema unificado."""
    return render(request, "sistema_unificado.html")


class ClienteListView(ListView):
    """Listado de clientes activos."""
    model = Cliente
    template_name = "clientes/list.html"
    context_object_name = "clientes"

    def get_queryset(self):
        return Cliente.objects.filter(activo=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clientes_activos"] = Cliente.objects.filter(activo=True)
        return context


class ClienteViewSet(viewsets.ModelViewSet):
    """API REST para clientes."""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    """API REST para reservas (relacionadas con clientes)."""
    queryset = Reserva.objects.select_related("cliente", "cabana").all()
    serializer_class = ReservaSerializer

"""
Vistas para la gestión de clientes.
"""
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from django.views import View
from .models import Cliente


def index(request):
    return render(request, "clientes/index.html")

class SistemaUnificadoView(View):
    """Vista que representa el sistema unificado."""
    def get(self, request):
        # lógica
        return HttpResponse("Sistema Unificado")
def listar_clientes(request):
    # lógica para listar clientes
    return render(request, "clientes/listar.html")
def index(request):
    # lógica para la página principal de clientes
    return render(request, "clientes/index.html")           

class ClienteListView(ListView):
    """Vista de lista que muestra todos los clientes registrados."""
    model = Cliente
    template_name = "clientes/lista_clientes.html"
    context_object_name = "clientes"

class ClienteCreateView(CreateView):
    """Vista de creación que permite registrar un nuevo cliente."""
    model = Cliente
    template_name = "clientes/formulario_clientes.html"
    fields = ["nombre", "apellido", "dni", "direccion", "telefono"]
    success_url = reverse_lazy("clientes:list")

class ClienteDetailView(DetailView):
    """Vista de detalle que muestra la información de un cliente específico."""
    model = Cliente
    template_name = "clientes/detalle_cliente.html"
    context_object_name = "cliente"

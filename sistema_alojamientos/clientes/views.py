"""
Vistas para la gestión de clientes.
"""
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.views import View
from .models import Cliente

def respuesta_root(request):
    return render(request, "respuesta_root.html")

def sistema_unificado(request):
    return render(request, "sistema_unificado.html")

def dashboard(request):
    return render(request, "dashboard.html")



def index(request): # pylint: disable=unused-argument
    return HttpResponse("Clientes funcionando")

class ClienteListView (ListView):
    model = Cliente
    template_name = "clientes/lista_clientes.html"
    context_object_name = "clientes"

    def get(self, request, *args, **kwargs):
        return HttpResponse("Lista de clientes")

class SistemaUnificadoView(View):
    def get(self, request):
        # lógica
        return HttpResponse("Sistema Unificado")
def listar_clientes(request):
    """ lista clientes"""
    return render(request, "clientes/listar.html")
        
class ClienteCreateView(CreateView):  # pylint: disable=too-many-ancestors
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

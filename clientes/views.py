"""
Vistas para la gestión de clientes.
"""
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import View
from .models import Cliente

class HomeView(View):
    """Vista principal que redirige a la lista de clientes."""
    def get(self, request, *args, **kwargs):
        """Redirige la solicitud a la lista de clientes."""
        return redirect("clientes:list")

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

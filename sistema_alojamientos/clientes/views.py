"""
Vistas 
"""
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Cliente
from rest_framework import viewsets
from .serializers import ClienteSerializer

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})

def SistemaUnificadoView(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})


class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'  # Ruta de tu plantilla para listar
    context_object_name = 'clientes'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'clientes/cliente_detail.html'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'correo', 'telefono']  # Ajusta según los campos de tu modelo
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('cliente_list')  # Redirige al listado al crear con éxito

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'correo', 'telefono']
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')
class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite realizar operaciones CRUD completas sobre Clientes.
    - GET /clientes/ (Listar)
    - POST /clientes/ (Crear)
    - GET /clientes/{id}/ (Detalle)
    - PUT / PATCH /clientes/{id}/ (Actualizar)
    - DELETE /clientes/{id}/ (Borrar)
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    

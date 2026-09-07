""" views"""
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cabana

def panel_cabanas(request):
    """ Panel de cabañas del sistema de gestión """
    # Aquí podrías pasar datos reales de tus modelos
    contexto = {
        "titulo": "Panel de Cabañas",
        "mensaje": "Bienvenida al sistema de gestión de cabañas"
    }
    return render(request, "cabanas/panel.html", contexto)

# Listado de cabañas
class CabanaListView(ListView):
    """ Vista de listado de cabañas """
    model = Cabana
    template_name = "cabanas/cabana_list.html"
    context_object_name = "cabanas"

# Detalle de una cabaña
class CabanaDetailView(DetailView):
    """ Vista de detalle de una cabaña """
    model = Cabana
    template_name = "cabanas/cabana_detail.html"
    context_object_name = "cabana"

# Crear nueva cabaña
class CabanaCreateView(CreateView):
    """ Vista para crear una nueva cabaña """
    model = Cabana
    template_name = "cabanas/cabana_form.html"
    fields = ["nombre", "descripcion", "precio", "disponible"]
    success_url = reverse_lazy("cabanas:cabanas_list")

# Editar cabaña existente
class CabanaUpdateView(UpdateView):
    """ Vista para editar una cabaña existente """
    model = Cabana
    template_name = "cabanas/cabana_form.html"
    fields = ["nombre", "descripcion", "precio", "disponible"]
    success_url = reverse_lazy("cabanas:cabanas_list")

# Eliminar cabaña
class CabanaDeleteView(DeleteView):
    """ Vista para eliminar una cabaña """
    model = Cabana
    template_name = "cabanas/cabana_confirm_delete.html"
    success_url = reverse_lazy("cabanas:cabanas_list")

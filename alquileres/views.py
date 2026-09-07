"""Vistas para la aplicación de alquileres."""
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Alquiler

class AlquilerListView(ListView):
    """Vista para listar todos los alquileres del sistema."""
    model = Alquiler
    template_name = 'alquileres/alquiler_list.html'
    context_object_name = 'alquileres'

    def get_queryset(self):
        # Corregido: El return ahora está adentro del método con sus 8 espacios correspondientes
        return Alquiler.objects.all()  # pylint: disable=no-member

class AlquilerDetailView(DetailView):
    """Vista para ver el detalle de un alquiler específico."""
    model = Alquiler
    template_name = 'alquileres/alquiler_detail.html'
    context_object_name = 'alquiler'

class AlquilerCreateView(CreateView):
    """Vista para registrar y crear un nuevo alquiler."""
    model = Alquiler
    fields = ['cliente', 'cabana', 'fecha_ingreso', 'hora_ingreso', 'fecha_salida', 'hora_salida']
    template_name = 'alquileres/alquiler_form.html'
    success_url = reverse_lazy('alquileres:list')

class AlquilerUpdateView(UpdateView):
    """Vista para editar o actualizar un alquiler existente."""
    model = Alquiler
    fields = ['cliente', 'cabana', 'fecha_ingreso', 'hora_ingreso', 'fecha_salida', 'hora_salida']
    template_name = 'alquileres/alquiler_form.html'
    success_url = reverse_lazy('alquileres:list')

class AlquilerDeleteView(DeleteView):
    """Vista para eliminar un alquiler del sistema."""
    model = Alquiler
    template_name = 'alquileres/alquiler_confirm_delete.html'
    success_url = reverse_lazy('alquileres:list')

"""Views de la aplicación Template."""
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from template.models import Template  # asegúrate de tener un modelo Template definido en models.py

class TemplateListView(ListView):
    """Vista para listar todas las plantillas."""
    model = Template
    template_name = "template/template_list.html"
    context_object_name = "templates"

class TemplateCreateView(CreateView):
    """Vista para crear una nueva plantilla."""
    model = Template
    template_name = "template/template_form.html"
    fields = ["nombre", "descripcion"]  # ajusta según los campos de tu modelo
    success_url = reverse_lazy("template:template_lista")

class TemplateDetailView(DetailView):
    """Vista para ver los detalles de una plantilla."""
    model = Template
    template_name = "template/template_detail.html"
    context_object_name = "template"

class TemplateUpdateView(UpdateView):
    """Vista para actualizar una plantilla existente."""
    model = Template
    template_name = "template/template_form.html"
    fields = ["nombre", "descripcion"]
    success_url = reverse_lazy("template:template_lista")

class TemplateDeleteView(DeleteView):
    """Vista para eliminar una plantilla."""
    model = Template
    template_name = "template/template_confirm_delete.html"
    success_url = reverse_lazy("template:template_lista")

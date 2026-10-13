# Vistas HTML (Class-Based Views)
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Cabana
from .forms import CabanaForm

class IndexView(TemplateView):
    template_name = "index.html"

class CabanaListView(ListView):
    model = Cabana
    template_name = "listar_cabanas.html"
    context_object_name = "cabanas"

class CabanaDetailView(DetailView):
    model = Cabana
    template_name = "detalle_cabana.html"
    context_object_name = "cabana"

class CabanaCreateView(CreateView):
    model = Cabana
    form_class = CabanaForm
    template_name = "crear_cabana.html"
    success_url = reverse_lazy("listar_cabanas")

class CabanaUpdateView(UpdateView):
    model = Cabana
    form_class = CabanaForm
    template_name = "editar_cabana.html"

    def get_success_url(self):
        return reverse_lazy("detalle_cabana", kwargs={"pk": self.object.pk})


# API REST (ViewSet con DRF)
from rest_framework import viewsets
from .serializers import CabanaSerializer

class CabanaViewSet(viewsets.ModelViewSet):
    queryset = Cabana.objects.all()
    serializer_class = CabanaSerializer

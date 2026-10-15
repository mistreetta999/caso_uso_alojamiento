# Vistas HTML (Class-Based Views)
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy
from .models import Cabana
from .forms import CabanaForm
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido a Alojamientos 🚀")

def index(request):
    cabanas = Cabana.objects.all()
    return render(request, "cabanas/index.html", {"cabanas": cabanas})

def nueva(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        capacidad = request.POST["capacidad"]
        precio = request.POST["precio"]
        Cabana.objects.create(nombre=nombre, capacidad=capacidad, precio=precio)
        return redirect("cabanas:index")
    return render(request, "cabanas/nueva.html")

def detalle(request, cabana_id):
    cabana = get_object_or_404(Cabana, pk=cabana_id)
    return render(request, "cabanas/detalle.html", {"cabana": cabana})

def editar(request, cabana_id):
    cabana = get_object_or_404(Cabana, pk=cabana_id)
    if request.method == "POST":
        cabana.nombre = request.POST["nombre"]
        cabana.capacidad = request.POST["capacidad"]
        cabana.precio = request.POST["precio"]
        cabana.save()
        return redirect("cabanas:index")
    return render(request, "cabanas/editar.html", {"cabana": cabana})


def crear_cabana(request):
    if request.method == "POST":
        form = CabanaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CabanaForm()
    return render(request, "crear_cabana.html", {"form": form})

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

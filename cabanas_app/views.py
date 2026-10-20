# Importaciones al inicio
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from .models import Cabana
from .serializers import CabanaSerializer 

def  lista_cabanas(request):
    cabanas = Cabana.objects.all()
    return render(request, "cabanas_app/lista.html", {"cabanas": cabanas})

def respuesta_root(request):
    return render(request, "respuesta_root.html")

def sistema_unificado(request):
    return render(request, "sistema_unificado.html")

def index(request):
    cabanas = Cabana.objects.all()
    return render(request, "cabanas_app/index.html", {"cabanas": cabanas})

def detalle_cabana(request, id):
    cabana = get_object_or_404(Cabana, pk=id)
    return render(request, "cabanas_app/detalle.html", {"cabana": cabana})

def nueva_cabana(request):
    """ nueva cabana"""
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        capacidad = request.POST.get("capacidad")
        Cabana.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            capacidad=capacidad
        )
        return redirect("cabanas:index")
    return render(request, "cabanas_app/nueva.html")



class CabanaListView(ListView):
    model = Cabana
    template_name = "cabanas_app/lista.html"
    context_object_name = "cabanas"

class CabanaDetailView(DetailView):
    model = Cabana
    template_name = "cabanas_app/detalle.html"
    context_object_name = "cabana"

class CabanaCreateView(CreateView):
    model = Cabana
    template_name = "cabanas_app/crear.html"
    fields = ["nombre", "descripcion", "capacidad"]

class CabanaUpdateView(UpdateView):
    model = Cabana
    template_name = "cabanas_app/actualizar.html"
    fields = ["nombre", "descripcion", "capacidad"]

class CabanaDeleteView(DeleteView):
    model = Cabana
    template_name = "cabanas_app/eliminar.html"
    success_url = "/cabanas/"

# -------------------------------
# ViewSet para API REST
# -------------------------------

class CabanaViewSet(viewsets.ModelViewSet):
    queryset = Cabana.objects.all()
    serializer_class = CabanaSerializer

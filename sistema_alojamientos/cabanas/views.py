import os
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Cabana
from sistema_alojamientos.alojamientos.models import Alojamiento
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido a Alojamientos 🚀")

def cabanas(request):
    return HttpResponse("Bienvenida a las cabanas")
def index(request):
    return HttpResponse("Bienvenida cabanas")

def lista_cabanas(request):
    """Vista para listar todas las cabañas."""
    cabanas = Cabana.objects.all()
    return render(request, "cabanas/lista.html", {"cabanas": cabanas})

def lista_cabanas_vistas(request):
    """Vista para listar todas las cabañas (vistas)."""
    cabanas = Cabana.objects.all()
    return render(request, "cabanas/lista.html", {"cabanas": cabanas})

# Vista de inicio
class InicioView(View):
    """Vista para la página de inicio."""
    def get(self, request):
        return render(request, "cabanas/inicio.html")

# Vista unificada
class SistemaUnificadoView(View):
    def get(self, request):
        contexto = {
            "cabanas": Cabana.objects.all(),
            "alojamientos": Alojamiento.objects.all(),
        }
        return render(request, "cabanas/sistema_unificado.html", contexto)

# Vista lista de alojamientos
def lista_alojamientos(request):
    """Vista para listar todos los alojamientos."""
    alojamientos = Alojamiento.objects.all()
    return render(request, "cabanas/lista_alojamientos.html", {"alojamientos": alojamientos})



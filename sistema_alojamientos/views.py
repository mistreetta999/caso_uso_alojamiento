from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from reservas_app.models import Reserva

from reservas_app.forms import ReservaForm

def crear_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reservas:list")  # ajustá al nombre de tu lista
    else:
        form = ReservaForm()
    return render(request, "reservas/crear_reserva.html", {"form": form})


def respuesta_root(request):
    return render(request, "respuesta_root.html")

def sistema_unificado(request):
    return render(request, "sistema_unificado.html")

def dashboard(request):
    return render(request, "dashboard.html")

def inicio(request):
    return render(request, "inicio.html")

class InicioView(TemplateView):
    template_name = "inicio.html"

class AyudaView(View):
    def get(self, request):
        return render(request, "ayuda.html")

class ContactoView(View):
    def get(self, request):
        return render(request, "contacto.html")

class SistemaUnificadoView(View):
    def get(self, request):
        return render(request, "sistema_unificado.html")

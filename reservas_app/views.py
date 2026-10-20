from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets

from reservas_app.models import Reserva

from .serializers import ReservaSerializer
from .forms import ReservaForm



def sistema_unificado(request):
    return render(request, "sistema_unificado.html")

def dashboard(request):
    return render(request, "dashboard.html")

def index(request):
    """Vista de índice para reservas."""
    return HttpResponse("Alojamientos")


def crear_reserva(request):
    """Formulario para crear una reserva."""
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ReservaForm()
    return render(request, "crear_reserva.html", {"form": form})


class ReservaViewSet(viewsets.ModelViewSet):
    """API REST para reservas."""
    queryset = Reserva.objects.select_related("cliente", "cabana", "alojamiento").all()
    serializer_class = ReservaSerializer



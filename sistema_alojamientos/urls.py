from django.urls import path
from django.shortcuts import render

def sistema_unificado(request):
    return render(request, "sistema_unificado.html")

urlpatterns = [
    path("", sistema_unificado, name="home"),
    path("clientes/", sistema_unificado),
    path("reservas/", sistema_unificado),
    path("cabanas/", sistema_unificado),
    path("alojamientos/", sistema_unificado),
]

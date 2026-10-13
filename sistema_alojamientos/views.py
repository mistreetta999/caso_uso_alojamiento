from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class InicioView(View):
    """Vista de inicio del sistema."""
    def get(self, request):
        return render(request, "inicio.html")


class SistemaUnificadoView(View):
    """Vista que representa el sistema unificado."""
    def get(self, request):
        return render(request, "sistema_unificado.html")


def dashboard(request):
    """Renderiza la página principal del dashboard."""
    return render(request, "dashboard.html")


def health_check(request):
    """Endpoint simple para verificar que el sistema está vivo."""
    return HttpResponse("Sistema alojamientos activo ✅")

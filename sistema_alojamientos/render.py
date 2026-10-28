from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Vistas simples con funciones
def dashboard(request):
    """
    Dashboard principal con accesos a todas las apps.
    """
    return render(request, "global/dashboard.html")

def inicio(request):
    """
    Página de inicio del sistema.
    """
    return render(request, "inicio.html")

def sistema_unificado(request):
    """
    Vista del sistema unificado.
    """
    return render(request, "sistema_unificado.html")  # o global/bootstrap.html

# Ejemplo de vistas basadas en clases
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


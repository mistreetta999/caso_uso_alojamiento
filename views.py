from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Vista principal del sistema
class InicioView(TemplateView):
    template_name = "inicio.html"   # asegurate de tener este template en tu carpeta templates

# Vista unificada del sistema


# Vista de ayuda o información
class AyudaView(View):
    """Vista de ayuda o información del sistema."""
    def get(self, request):
        return render(request, "ayuda.html")

# Vista de contacto
class ContactoView(View):
    """Vista de contacto del sistema."""
    def get(self, request):
        return render(request, "contacto.html")

# Vista del sistema unificado
class SistemaUnificadoView(View):
    """Vista del sistema unificado."""
    def get(self, request):
        return render(request, "sistema_unificado.html")

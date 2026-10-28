from django.shortcuts import render

def dashboard(request):
    """
    Dashboard principal que muestra enlaces a todas las apps.
    """
    return render(request, "global/global/dashboard.html")

def inicio(request):
    """
    Vista de inicio simple.
    """
    return render(request, "inicio.html")

def sistema_unificado(request):
    """
    Vista del sistema unificado.
    """
    return render(request, "global/global/bootstrap.html")

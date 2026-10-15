from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer
from django.shortcuts import render, redirect
from .forms import ClienteForm
from django.http import HttpResponse

#def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ClienteForm()
    return render(request, "crear_cliente.html", {"form": form})

class ClienteViewSet(viewsets.ModelViewSet):
    """API REST para clientes."""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

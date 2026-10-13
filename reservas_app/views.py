from django.http import HttpResponse
from rest_framework import viewsets
from .models import Reserva
from .serializers import ReservaSerializer

def index(request):
    return HttpResponse("¡Bienvenido al sistema de alojamientos!")
class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
class ClienteReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.filter(cliente__isnull=False)
    serializer_class = ReservaSerializer
class ClienteDetalleViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.filter(cliente__isnull=False)
    serializer_class = ReservaSerializer
class ClienteReservaDetalleViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.filter(cliente__isnull=False)
    serializer_class = ReservaSerializer
class CabanaReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.filter(cabana__isnull=False)
    serializer_class = ReservaSerializer
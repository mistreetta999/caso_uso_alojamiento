import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from sistema_alojamientos.reservas.models import Reserva
from sistema_alojamientos.clientes.models import Cliente
from sistema_alojamientos.cabanas.models import Cabana
from sistema_alojamientos.alojamientos.models import Alojamiento

@pytest.mark.django_db
def test_crear_reserva():
    client = APIClient()

    # Crear datos base
    alojamiento = Alojamiento.objects.create(nombre="Hotel Mina", capacidad=50, precio=1000)
    cabana = Cabana.objects.create(alojamiento=alojamiento, nombre="Cabana 1", disponible=True)
    cliente = Cliente.objects.create(nombre="Carolina", apellido="Test", email="caro@test.com")

    # Datos de la reserva
    data = {
        "cliente": cliente.id,
        "cabana": cabana.id,
        "fecha_inicio": "2026-10-20",
        "fecha_fin": "2026-10-25",
        "precio_total": "5000.00"
    }

    url = reverse("reserva-list")  # nombre generado por el router de DRF
    response = client.post(url, data, format="json")

    assert response.status_code == 201
    assert Reserva.objects.count() == 1
    reserva = Reserva.objects.first()
    assert reserva.cliente == cliente
    assert reserva.cabana == cabana

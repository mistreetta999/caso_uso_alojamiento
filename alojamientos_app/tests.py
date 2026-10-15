from django.test import TestCase

from .models import Alojamiento
from reservas_app.models import Reserva

class AlojamientoModelTest(TestCase):
    def test_crear_alojamiento(self):
        alojamiento = Alojamiento.objects.create(
            nombre="Cabaña Test",
            ubicacion="Mina Clavero",
            precio_noche=1000.00,
            disponible=True
        )
        self.assertEqual(alojamiento.nombre, "Cabaña Test")
class ReservaTest(TestCase):
    def test_default_horas(self):
        reserva = Reserva.objects.create()  # crea sin horas
        self.assertEqual(reserva.hora_ingreso.strftime("%H:%M"), "10:00")
        self.assertEqual(reserva.hora_salida.strftime("%H:%M"), "10:00")
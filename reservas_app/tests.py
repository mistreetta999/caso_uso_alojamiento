from django.test import TestCase
from reservas_app.models import Reserva


class ReservaTestCase(TestCase):
    def setUp(self):
        Reserva.objects.create(cliente="Carolina", fecha_reserva="2026-10-13", cantidad_personas=2)

    def test_reserva_creada(self):
        reserva = Reserva.objects.get(cliente="Carolina")
        self.assertEqual(reserva.cantidad_personas, 2)

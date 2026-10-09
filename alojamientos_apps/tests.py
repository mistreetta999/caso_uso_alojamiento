from django.test import TestCase
from .models import Alojamiento

class AlojamientoModelTest(TestCase):
    def test_crear_alojamiento(self):
        alojamiento = Alojamiento.objects.create(
            nombre="Cabaña Test",
            ubicacion="Mina Clavero",
            precio_noche=1000.00,
            disponible=True
        )
        self.assertEqual(alojamiento.nombre, "Cabaña Test")

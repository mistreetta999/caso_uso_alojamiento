from django.test import TestCase
from django.urls import reverse
from .models import Cabana

class CabanaModelTest(TestCase):
    def setUp(self):
        self.cabana = Cabana.objects.create(
            nombre="Cabana Test",
            descripcion="Cabana de prueba",
            capacidad=4,
            precio_por_noche=1500.00,
            disponible=True
        )

    def test_cabana_str(self):
        """El método __str__ devuelve el nombre y capacidad."""
        self.assertEqual(str(self.cabana), "Cabana Test (capacidad: 4)")

    def test_cabana_disponible(self):
        """La cabaña creada está disponible por defecto."""
        self.assertTrue(self.cabana.disponible)


class CabanaViewsTest(TestCase):
    def setUp(self):
        self.cabana = Cabana.objects.create(
            nombre="Cabana Vista",
            descripcion="Vista de prueba",
            capacidad=2,
            precio_por_noche=800.00,
            disponible=True
        )

    def test_lista_cabanas_view(self):
        """La vista lista_cabanas devuelve status 200 y contiene el nombre."""
        url = reverse("lista_cabanas")  # asegúrate que exista en urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cabana Vista")


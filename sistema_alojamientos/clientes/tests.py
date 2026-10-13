from django.test import TestCase
from .models import Cliente

class ClienteModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre="Juan",
            apellido="Pérez",
            dni="12345678",
            email="juanperez@example.com",
            telefono="3515555555",
            direccion="Av. Siempre Viva 742"
        )

    def test_cliente_creado(self):
        """Verifica que el cliente se crea correctamente"""
        self.assertEqual(self.cliente.nombre, "Juan")
        self.assertEqual(self.cliente.apellido, "Pérez")
        self.assertEqual(self.cliente.dni, "12345678")

    def test_str_cliente(self):
        """Verifica que el método __str__ devuelve nombre y apellido"""
        self.assertEqual(str(self.cliente), "Juan Pérez")

from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Cliente

class ClienteModelTest(TestCase):
    def test_model_exists(self):
        """Verifica que el modelo Cliente está definido"""
        self.assertTrue(hasattr(Cliente, '_meta'))

    def test_str_method(self):
        """Verifica que el método __str__ devuelve nombre y apellido"""
        cliente = Cliente(nombre="Juan", apellido="Pérez")
        self.assertEqual(str(cliente), "Juan Pérez")

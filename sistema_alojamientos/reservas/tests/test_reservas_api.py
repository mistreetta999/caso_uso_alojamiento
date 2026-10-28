from django.test import TestCase
from django.urls import reverse
# Si utilizas Django REST Framework para tus APIs, descomenta la siguiente línea:
# from rest_framework.test import APITestCase


class ReservasApiTests(TestCase): # Cambia a APITestCase si usas DRF
    """
    Pruebas unitarias e integrales para verificar el correcto funcionamiento 
    de los endpoints y la API del módulo de reservas.
    """

    def setUp(self):
        """
        Configuración inicial previa a la ejecución de cada prueba.
        Aquí puedes crear datos de prueba (fixtures) si los necesitas.
        """
        pass

    def test_lista_reservas_status_code(self):
        """
        Verifica que la URL o endpoint del listado de reservas responda 
        con un código HTTP 200 (OK).
        """
        # Intenta usar reverse si tienes nombrada la ruta, o usa la ruta directa por URL
        try:
            url = reverse('reservas:lista_reservas') # Ajusta el namespace si aplica
        except Exception:
            url = '/reservas/'

        response = self.client.get(url)
        # Se acepta 200 (éxito) o 302/301 si requiere autenticación y redirige al login
        self.assertIn(response.status_code, [200, 302])

    def test_crear_reserva_get_status_code(self):
        """
        Verifica que el formulario de creación de reservas cargue correctamente 
        o responda con una redirección si está protegido.
        """
        try:
            url = reverse('reservas:crear_reserva')
        except Exception:
            url = '/reservas/nuevo/'

        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 302])


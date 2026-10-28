# alojamientos_app/tests.py
from django.test import TestCase

class SimpleTest(TestCase):
    def test_suma(self):
        self.assertEqual(1 + 1, 2)


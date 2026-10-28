"""Modelos para la aplicación de alojamientos_apps."""
from django.db import models

# alojamientos_app/models.py
class Alojamiento(models.Model):
    nombre = models.CharField(max_length=100)
    precio_noche = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # nombre esperado
    capacidad = models.IntegerField()
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200, default="Mina Clavero")
    disponible = models.BooleanField(default=True)  # campo esperado

    def __str__(self):
        return str(self.nombre)


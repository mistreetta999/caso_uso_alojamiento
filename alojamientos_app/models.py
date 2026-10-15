"""Modelos para la aplicación de alojamientos_apps."""
from django.db import models

class Alojamiento(models.Model):
    nombre = models.CharField(max_length=100)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    capacidad = models.IntegerField()
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200, default="Mina Clavero")

    def __str__(self) -> str:
        return str(self.nombre)

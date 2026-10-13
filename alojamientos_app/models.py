"""Modelos para la aplicación de alojamientos_apps."""
from django.db import models

class Alojamiento(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    capacidad = models.PositiveIntegerField(default=1)
    descripcion = models.TextField(default="Sin descripción")

    def __str__(self):
        return self.nombre

"""Modelos de alojamientos disponibles en el sistema."""

from django.db import models
class Alojamiento(models.Model):
    """ alojamientos"""
    nombre = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.nombre)
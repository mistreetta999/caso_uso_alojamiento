"""
Modelos para la aplicación 'cabanas'.
"""
from django.db import models

class Cabana(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()   # ahora sí existe
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

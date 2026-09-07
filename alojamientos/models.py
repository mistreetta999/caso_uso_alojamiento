"""Modelos de alojamientos disponibles en el sistema."""

from django.db import models

class Alojamiento(models.Model):
    """Modelo que representa un alojamiento disponible en el sistema."""    
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    capacidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """Metadatos del modelo Alojamiento."""
        verbose_name = "Alojamiento"
        verbose_name_plural = "Alojamientos"
    
    def __str__(self):
        return f"{self.nombre} - {self.direccion}"
    
from django.db import models
from typing import Any

class Cabana(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    capacidad = models.PositiveIntegerField(default=1)
    descripcion = models.TextField(default="Sin descripción")

    # Esto ayuda al IDE a reconocer el manager
    objects: Any

    def __str__(self) -> str:
        return str(self.nombre)

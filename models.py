"""
Modelos de la aplicación de alojamientos.
"""
from django.db import models

class Cliente(models.Model):
    """Modelo que representa a un cliente."""
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_ingreso = models.DateField()
    hora_ingreso = models.TimeField()
    fecha_salida = models.DateField()
    hora_salida = models.TimeField()

    def __str__(self):
        return str(f"{self.nombre} ({self.dni})")


class Cabana(models.Model):
    """Modelo que representa a una cabaña."""
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.nombre)


class Alquiler(models.Model):
    """Modelo que representa un alquiler de cabaña por un cliente."""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return str(f"{self.cliente} - {self.cabana}")

"""Modelos para la aplicación de clientes."""
from django.db import models

class Cliente(models.Model):
    """
    Modelo que representa datos de un cliente.
    """
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True, verbose_name="DNI")
    direccion = models.TextField(blank=True, null=True, verbose_name="Dirección")
    telefono = models.CharField(max_length=20, blank=True)

    class Meta:
        """ Metadatos del modelo Cliente. """
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

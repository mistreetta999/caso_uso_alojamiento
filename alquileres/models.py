"""Modelos de la aplicación 'alquileres'."""
from django.db import models

class Alquiler(models.Model):
    """Modelo que representa un alquiler de cabaña."""
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    cabana = models.ForeignKey('cabanas.Cabana', on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    hora_ingreso = models.TimeField()
    fecha_salida = models.DateField()
    hora_salida = models.TimeField()

    class Meta:
        """Metadatos del modelo Alquileres."""
        app_label = 'alquileres'  # <-- AGREGÁ ESTA LÍNEA AQUÍ
        verbose_name = "Alquiler"
        verbose_name_plural = "Alquileres"

    def __str__(self):
        return f"Alquiler de {self.cabana} por {self.cliente}"


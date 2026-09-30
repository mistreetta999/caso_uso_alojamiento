"""Modelos de la aplicación 'reservas'."""
from django.db import models

class Reserva(models.Model):
    """Modelo que representa una reserva de cabaña."""
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    cabana = models.ForeignKey('cabanas.Cabana', on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    hora_ingreso = models.TimeField()
    fecha_salida = models.DateField()
    hora_salida = models.TimeField()

    class Meta:
        """Metadatos del modelo Reservas."""
        app_label = 'reservas'  # <-- AGREGÁ ESTA LÍNEA AQUÍ
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f"Reserva de {self.cabana} por {self.cliente}"


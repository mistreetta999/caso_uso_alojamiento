"""Modelo que representa una reserva de cabaña."""
import datetime
from django.db import models

class Reserva(models.Model):
    """Modelo que representa una reserva de cabaña."""
    cabana = models.ForeignKey('cabanas.Cabana', on_delete=models.CASCADE)
    fecha_inicio = models.DateField(default=datetime.date.today)
    fecha_fin = models.DateField(default=datetime.date.today)
    hora_ingreso = models.TimeField(default=datetime.time(10, 0))
    hora_salida = models.TimeField(default=datetime.time(10, 0))
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE, related_name='reservas_de_app_reservas')
    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f"Reserva de {self.cabana} por {self.cliente}"



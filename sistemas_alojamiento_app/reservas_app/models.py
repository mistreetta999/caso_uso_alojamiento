from django.db import models
from django.utils import timezone
import datetime

from sistemas_alojamiento_app.clientes_app.models import Cliente
from sistemas_alojamiento_app.cabanas_app.models import Cabana

class Reserva(models.Model):
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_fin = models.DateField(default=timezone.now)
    hora_ingreso = models.TimeField(default=datetime.time(10, 0))
    hora_salida = models.TimeField(default=datetime.time(10, 0))

    cabana = models.ForeignKey(
        Cabana,
        on_delete=models.CASCADE
    )

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="reservas_de_reservas_app"
    )

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f"Reserva de {self.cliente} - {self.cabana}"

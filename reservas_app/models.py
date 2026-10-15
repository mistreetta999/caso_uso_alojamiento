from django.db import models
import datetime

from clientes_app.models import Cliente
from cabanas_app.models import Cabana

class Reserva(models.Model):
    """Modelo que representa una reserva de una cabaña por un cliente."""
    cliente = models.ForeignKey('clientes_app.Cliente', on_delete=models.CASCADE)
    cabana = models.ForeignKey('cabanas_app.Cabana', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    hora_ingreso = models.TimeField(default=datetime.time(10, 0))
    hora_salida = models.TimeField(default=datetime.time(10, 0))


    class Meta:
        """Metadatos del modelo Reserva."""
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
     return f"Reserva de {self.cliente} - {self.cabana} ({self.fecha_inicio} a {self.fecha_fin})"
from django.db import models
import datetime

from clientes_app.models import Cliente
from cabanas_app.models import Cabana

class Reserva(models.Model):
    cabana = models.ForeignKey('cabanas_app.Cabana', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    hora_ingreso = models.TimeField(default=datetime.time(10, 0))
    hora_salida = models.TimeField(default=datetime.time(10, 0))
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas_de_reservas_app')
    
    class Meta:
        """Metadatos del modelo Reserva."""
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f"Reserva de {self.cliente} - {self.cabana} ({self.fecha_inicio} a {self.fecha_fin})"
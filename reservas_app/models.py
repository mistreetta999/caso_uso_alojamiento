from django.db import models

class Reserva(models.Model):
    # Ejemplo en reservas_app/models.py
    cabana = models.ForeignKey('cabanas_app.Cabana', on_delete=models.CASCADE)
    cliente = models.CharField(max_length=100)
    fecha_reserva = models.DateField()
    cantidad_personas = models.IntegerField()
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Reserva de {self.cliente} - {self.fecha_reserva}"

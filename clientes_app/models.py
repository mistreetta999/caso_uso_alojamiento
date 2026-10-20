from django.db import models

class Cliente(models.Model):
    """Modelo que representa a un cliente."""
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    reserva = models.CharField(max_length=100, default="ok")
    telefono = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"



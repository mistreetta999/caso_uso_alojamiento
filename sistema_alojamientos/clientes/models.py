from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    #

    telefono = models.CharField(max_length=20)
    reserva = models.CharField(max_length=100)   # campo que falta en la DB
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

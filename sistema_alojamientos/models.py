from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre


class Cabana(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Alojamiento(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    cabanas = models.ManyToManyField(Cabana, related_name="alojamientos")

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="reservas")
    alojamiento = models.ForeignKey(Alojamiento, on_delete=models.CASCADE, related_name="reservas")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"Reserva de {self.cliente} en {self.alojamiento}"


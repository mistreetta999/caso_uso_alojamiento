from django.db import models
from django import forms

# ============================
# MODELOS
# ============================

class Alojamiento(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    capacidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Alojamiento"
        verbose_name_plural = "Alojamientos"

    def __str__(self):
        return f"{self.nombre} - {self.direccion}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Alquiler(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    alojamiento = models.ForeignKey(Alojamiento, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        verbose_name = "Alquiler"
        verbose_name_plural = "Alquileres"

    def __str__(self):
        return f"{self.cliente} - {self.alojamiento}"


# ============================
# FORMULARIOS
# ============================

class AlojamientoForm(forms.ModelForm):
    class Meta:
        model = Alojamiento
        fields = ["nombre", "direccion", "capacidad", "precio"]


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "apellido", "dni", "telefono"]


class AlquilerForm(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = ["cliente", "alojamiento", "fecha_inicio", "fecha_fin"]

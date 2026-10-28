"""Modelos para las cabañas del sistema de alojamiento."""

from django.db import models
from django.db.models.fields import BooleanField, CharField, IntegerField, TextField

# cabanas_app/models.py
class Cabana(models.Model):
    """ class cabana"""
    nombre = CharField(max_length=100)
    capacidad = IntegerField()
    descripcion = TextField()
    disponible = BooleanField(default=True)  # campo esperado

    def __str__(self):
        return f"{self.nombre} (capacidad: {self.capacidad})"



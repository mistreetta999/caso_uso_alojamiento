from rest_framework import serializers
from django.contrib.auth.models import User 

from .models import Reserva


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = [
            "id",
            "fecha_reserva",  # fecha en que se realizó la reserva
            "fecha_inicio",
            "fecha_fin",
            "cliente",        # relación con Cliente
            "alojamiento",    # relación con Alojamiento o Cabana
            "fecha_inicio",
            "fecha_fin",
            "estado"
        ]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]



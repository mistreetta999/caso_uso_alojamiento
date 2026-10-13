from rest_framework import serializers
from .models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = [
            "id",
            "cliente",        # relación con Cliente
            "alojamiento",    # relación con Alojamiento o Cabana
            "fecha_inicio",
            "fecha_fin",
            "estado"
        ]

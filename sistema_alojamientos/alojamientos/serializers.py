# sistema_alojamientos/alojamientos/serializers.py
from rest_framework import serializers
from sistema_alojamiento.models import Alojamiento, Cabana, Cliente, Reserva
from rest_framework import serializers
from reservas_app.models import Reserva


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = "__all__"

class AlojamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alojamiento
        fields = "__all__"


class CabanaSerializer(serializers.ModelSerializer):
    alojamiento = serializers.StringRelatedField()  # muestra el nombre del alojamiento

    class Meta:
        model = Cabana
        fields = "__all__"


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class ReservaSerializer(serializers.ModelSerializer):
    cliente = serializers.StringRelatedField()
    cabana = serializers.StringRelatedField()

    class Meta:
        model = Reserva
        fields = "__all__"

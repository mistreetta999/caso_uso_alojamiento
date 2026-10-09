from rest_framework import serializers
from .models import Alojamiento

class AlojamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alojamiento
        fields = "__all__"

from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'  # Esto incluye todos los campos del modelo Cliente automáticamente
        # O si prefieres campos específicos, puedes listarlos así:
        # fields = ['id', 'nombre', 'apellido', 'correo', 'telefono']

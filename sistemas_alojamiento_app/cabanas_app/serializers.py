from rest_framework import serializers
from .models import Cabana

class CabanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabana
        fields = "__all__"


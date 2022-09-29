from dataclasses import field
from rest_framework import serializers
from restaurante.models import prato

class PratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = prato
        fields = '__all__'
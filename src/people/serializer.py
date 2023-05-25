from rest_framework import serializers
from src.people.models import Persona

class AdminPersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ("id", "nombres", "apellidos", "email")
        read_only = ("id", )
from rest_framework import serializers
from inventario.models import EquipoUsuario, Equipo

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = "__all__"


class EquipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipoUsuario
        fields = "__all__"
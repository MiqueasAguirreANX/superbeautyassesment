from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication, permissions
from inventario.models import Equipo, EquipoUsuario
from inventario.serializers import EquipoSerializer, EquipoUsuarioSerializer

# Create your views here.

class GetAllEquiposAPIView(APIView):
    """
    View to list all equipos
    """
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        equipos = Equipo.objects.all().values()
        return Response(equipos)


class EquipoViewSet(viewsets.ModelViewSet):
    """
    Equipo model ViewSet
    """
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    permission_classes = [permissions.IsAdminUser]


class EquipoUsuarioViewSet(viewsets.ModelViewSet):
    """
    Equipo Usuario model ViewSet
    """
    queryset = EquipoUsuario.objects.all()
    serializer_class = EquipoUsuarioSerializer
    permission_classes = [permissions.IsAdminUser]

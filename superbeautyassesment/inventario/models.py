from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Equipo(models.Model):
    referencia = models.CharField(max_length=250)
    marca = models.CharField(max_length=250)
    procesador = models.CharField(max_length=250)
    memoria = models.CharField(max_length=250)
    disco = models.CharField(max_length=250)
    tipo = models.CharField(max_length=250)


class EquipoUsuario(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()
    fecha_entrega = models.DateField()
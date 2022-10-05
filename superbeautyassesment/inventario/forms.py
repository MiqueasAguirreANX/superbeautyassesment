from django import forms
from inventario.models import EquipoUsuario, Equipo
from django.contrib.auth.models import User


class EquipoUsuarioAdminForm(forms.ModelForm):
    equipo = forms.ModelChoiceField(queryset=Equipo.objects.filter(equipousuario__usuario=None))

    class Meta:
        model = EquipoUsuario
        fields = '__all__'
from dataclasses import fields

from rest_framework import serializers
from .models import Mascota, Historia_Clinica, Medicamento


class MascotaSerializable(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = (
            'nombre',
            'edad',
            'raza',
            'tipo',
            'duenio'
        )

class Historia_ClinicaSerializable(serializers.ModelSerializer):
    class Meta:
        model = Historia_Clinica
        fields = (
            'numero_historia',
            'fehca_creacion',
            'fecha_revision',
            'diagnostico'
        )

class MedicamentoSerializable(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = (
            'nombre_medicamento',
            'tipo_medicamento',
            'precio_medicamento',
            'fecha_caducidad'
        )

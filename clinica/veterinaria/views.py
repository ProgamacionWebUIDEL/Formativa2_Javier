from django.shortcuts import render
from rest_framework import viewsets
from .serializer import MascotaSerializable, Historia_ClinicaSerializable, MedicamentoSerializable
from .models import Mascota, Historia_Clinica, Medicamento

# Create your views here.

class MascotaVista(viewsets.ModelViewSet):
    serializer_class:MascotaSerializable
    queryset = Mascota.objects.all()

class Historia_ClinicaVista(viewsets.ModelViewSet):
    serializer_class:Historia_ClinicaSerializable
    queryset = Historia_Clinica.objects.all()

class MedicamentoVista(viewsets.ModelViewSet):
    serializer_class:MedicamentoSerializable
    queryset = Medicamento.objects.all()

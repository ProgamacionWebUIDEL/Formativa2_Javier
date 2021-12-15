from django.db import models

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=200, help_text="Nombre de la Mascota")
    edad = models.IntegerField(help_text="Edad en años de la Mascota")
    raza = models.CharField(max_length=120, help_text="Raza de la Mascota")
    tipo = models.CharField(max_length=120, help_text="Tipo de Mascota")
    duenio = models.CharField(max_length=120, help_text="Nombre del dueño de la Mascota")

class Historia_Clinica(models.Model):
    numero_historia = models.IntegerField(help_text="Número Único de la Historia CLinica")
    fecha_creacion = models.DateTimeField(help_text="Fecha de Ingreso de la Mascota a la CLinica")
    fecha_revision = models.DateTimeField(help_text="Fecha de Revision de la Mascota")
    diagnostico = models.CharField(max_length=1000, help_text="Diagnostico de la Mascota")

class Medicamento(models.Model):
    nombre_medicamento = models.CharField(max_length=200, help_text="Nombre del Medicamento")
    tipo_medicamento = models.CharField(max_length=120, help_text="Tipo de Medicamento")
    precio_medicamento = models.FloatField(max_length=200, help_text="Precio de Venta del Medicamento")
    fecha_caducidad = models.DateTimeField(help_text="Fecha de Caducidad del Medicamento")

from django.db import models
from django.utils.timezone import now

# Create your models here.

class Socio(models.Model):
    nombreSocio = models.CharField(max_length=100)
    fechaAlta = models.DateField(default=now, editable=False)

class Pista(models.Model):
    tipoSuperficie = models.CharField(max_length=255)
    enMantenimiento = models.BooleanField(default=False)

class Reserva(models.Model):
    socio = models.ForeignKey('Socio', on_delete=models.SET_NULL, null=True)
    pista = models.ForeignKey('Pista', on_delete=models.SET_NULL, null=True)
    fechaReserva = models.DateField(default=now)
    horaReserva = models.IntegerField()

# Populate database
# This file has to be placed within the
# catalog/management/commands directory in your project.
# If that directory doesn't exist, create it.
# The name of the script is the name of the custom command,
# that is, populate.py.
#
# execute python manage.py  populate

import os

from django.core.management.base import BaseCommand
from examen.models import (Socio, Pista, Reserva)


# The name of this class is not optional must be Command
# otherwise manage.py will not process it properly
#


class Command(BaseCommand):
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = """populate database
           """

    def handle(self, *args, **kwargs):
        self.socio()
        self.pista()
        self.reserva()

    def cleanDataBase(self):
        pass

    def socio(self):
        " Insert users"
        socio = Socio(id=1001, nombreSocio='socio_01', fechaAlta='2019-04-08')
        socio.save()
        socio = Socio(id=1002, nombreSocio='socio_02', fechaAlta='2020-07-14')
        socio.save()
        socio = Socio(id=1003, nombreSocio='socio_03', fechaAlta='2021-03-08')
        socio.save()

    def pista(self):
        " Insert authors"
        pista = Pista(id=1001, tipoSuperficie='césped artificial', enMantenimiento=False)
        pista.save()
        pista = Pista(id=1002, tipoSuperficie='resina sintética', enMantenimiento=False)
        pista.save()
        pista = Pista(id=1003, tipoSuperficie='cemento', enMantenimiento=True)
        pista.save()

    def reserva(self):
        " Insert authors"
        reserva = Reserva(socio=Socio.objects.filter(id=1001).first(), pista=Pista.objects.filter(id=1001).first(), fechaReserva='2021-03-21', horaReserva=12)
        reserva.save()
        reserva = Reserva(socio=Socio.objects.filter(id=1002).first(), pista=Pista.objects.filter(id=1001).first(), fechaReserva='2021-07-21', horaReserva=19)
        reserva.save()
        reserva = Reserva(socio=Socio.objects.filter(id=1003).first(), pista=Pista.objects.filter(id=1002).first(), fechaReserva='2021-05-25', horaReserva=17)
        reserva.save()
        reserva = Reserva(socio=Socio.objects.filter(id=1002).first(), pista=Pista.objects.filter(id=1003).first(), fechaReserva='2021-08-22', horaReserva=22)
        reserva.save()



















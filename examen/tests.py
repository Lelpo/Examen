from django.test import TestCase, Client
from .models import Socio, Pista, Reserva
from django.urls import reverse
# Create your tests here.

class ModelTests(TestCase):

    def test(self):
        Socio.objects.all().delete()
        Pista.objects.all().delete()
        Reserva.objects.all().delete()
        socio = Socio(id=1001, nombreSocio='Socio1', fechaAlta='2021-09-21')
        socio.save()
        socio = Socio(id=1002, nombreSocio='Socio2', fechaAlta='2021-10-15')
        socio.save()
        pista = Pista(id=1001, tipoSuperficie='césped artificial', enMantenimiento=False)
        pista.save()
        reserva = Reserva(socio=Socio.objects.filter(id=1001).first(), pista=Pista.objects.filter(id=1001).first(), fechaReserva='2021-11-08', horaReserva=10)
        reserva.save()
        reserva = Reserva(socio=Socio.objects.filter(id=1002).first(), pista=Pista.objects.filter(id=1001).first(), fechaReserva='2021-11-15', horaReserva=20)
        reserva.save()

        response = self.client.get(reverse('socio_detail', kwargs={'pk': 1001}), follow=True)
        reserva = Reserva.objects.filter(socio__id=1001).first()
        self.assertEqual(reserva, response.context['reservas'][0], "reservas incorrectas")



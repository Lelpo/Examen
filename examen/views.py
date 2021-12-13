from django.shortcuts import render
from .models import Socio, Reserva

# Create your views here.

def socio_detail(request, pk):
    socio = Socio.objects.filter(id=pk).first()
    reservas = Reserva.objects.filter(socio__id=pk)
    context = {'socio': socio, 'reservas': reservas}
    return render(request, 'socio_detail.html', context=context)

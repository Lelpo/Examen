from django.contrib import admin

# Register your models here.

from .models import Socio, Pista, Reserva

admin.site.register(Socio)
admin.site.register(Pista)
admin.site.register(Reserva)


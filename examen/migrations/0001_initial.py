# Generated by Django 3.2.6 on 2021-12-13 08:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoSuperficie', models.CharField(max_length=255)),
                ('enMantenimiento', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreSocio', models.CharField(max_length=100)),
                ('fechaAlta', models.DateField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaReserva', models.DateField(default=django.utils.timezone.now)),
                ('horaReserva', models.IntegerField()),
                ('pista', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='examen.pista')),
                ('socio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='examen.socio')),
            ],
        ),
    ]

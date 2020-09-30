# Generated by Django 3.0.7 on 2020-08-23 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prenotazioni', '0004_auto_20200705_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnagraficaScuole',
            fields=[
                ('codice_ministeriale', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('indirizzo', models.CharField(blank=True, max_length=50)),
                ('comune', models.CharField(blank=True, max_length=50)),
                ('provincia', models.CharField(blank=True, max_length=50)),
                ('tiposcuola', models.CharField(blank=True, max_length=50)),
                ('telefono', models.CharField(blank=True, max_length=40)),
            ],
        ),
    ]
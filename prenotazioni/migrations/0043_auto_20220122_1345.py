# Generated by Django 3.0.7 on 2022-01-22 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prenotazioni', '0042_movimentiprenotazione_orario'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimentiprenotazione',
            name='orario_turno',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='movimentiprenotazione',
            name='settore',
            field=models.CharField(max_length=31, null=True),
        ),
    ]
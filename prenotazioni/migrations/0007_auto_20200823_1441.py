# Generated by Django 3.0.7 on 2020-08-23 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prenotazioni', '0006_auto_20200823_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimentiprenotazione',
            name='nome_scuola',
        ),
        migrations.AddField(
            model_name='prenotazione',
            name='nome_scuola',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

# Generated by Django 3.0.7 on 2021-02-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prenotazioni', '0032_auto_20210205_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='prenotazione',
            name='ora',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prenotazione',
            name='scuola',
            field=models.BooleanField(default=True, null=True),
        ),
    ]

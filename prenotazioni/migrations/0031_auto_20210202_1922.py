# Generated by Django 3.0.7 on 2021-02-02 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prenotazioni', '0030_auto_20210202_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prenotazione',
            name='argomentiPreferiti',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

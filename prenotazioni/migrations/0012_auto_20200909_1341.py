# Generated by Django 3.0.7 on 2020-09-09 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prenotazioni', '0011_auto_20200909_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prenotazione',
            name='status',
            field=models.CharField(choices=[('DC', 'Da Confermare'), ('CO', 'Confermato')], default='DC', max_length=2, null=True),
        ),
    ]

# Generated by Django 3.0.7 on 2020-09-21 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prenotazioni', '0014_auto_20200912_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='TabellaRuoli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruolo', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'ruolo',
                'verbose_name_plural': 'ruoli',
            },
        ),
    ]

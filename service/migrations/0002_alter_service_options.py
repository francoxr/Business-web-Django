# Generated by Django 3.2.5 on 2021-12-18 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['created_at'], 'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
    ]

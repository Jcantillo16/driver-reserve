# Generated by Django 4.1.3 on 2022-11-06 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0003_remove_driver_location_driver_lastupdate_driver_lat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='lastUpdate',
            field=models.DateTimeField(),
        ),
    ]

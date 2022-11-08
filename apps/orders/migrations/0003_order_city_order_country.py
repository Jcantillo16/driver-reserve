# Generated by Django 4.1.3 on 2022-11-08 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_latitude_alter_order_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(blank=True, default='Colombia', max_length=100, null=True),
        ),
    ]

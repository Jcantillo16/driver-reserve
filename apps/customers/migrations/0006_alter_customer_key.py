# Generated by Django 4.1.3 on 2022-11-06 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_alter_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='key',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-06 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_payment_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

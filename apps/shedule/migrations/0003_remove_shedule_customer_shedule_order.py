# Generated by Django 4.1.3 on 2022-11-08 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_order_status'),
        ('shedule', '0002_shedule_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shedule',
            name='customer',
        ),
        migrations.AddField(
            model_name='shedule',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_shedule', to='orders.order'),
        ),
    ]

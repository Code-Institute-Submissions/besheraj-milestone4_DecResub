# Generated by Django 3.1.2 on 2020-11-14 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20201107_0403'),
        ('checkout', '0002_remove_order_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='service_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='services.service'),
        ),
    ]
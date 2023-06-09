# Generated by Django 3.2.18 on 2023-05-04 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_client_is_active'),
        ('loaders', '0008_auto_20230501_1454'),
        ('orders', '0002_auto_20230504_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pay_method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='loaders.paymethod'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
        ),
    ]

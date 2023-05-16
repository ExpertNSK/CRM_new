# Generated by Django 3.2.18 on 2023-05-14 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('passports', '0001_initial'),
        ('loaders', '0009_auto_20230514_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loader',
            name='passport',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='passport', to='passports.passport'),
        ),
        migrations.AlterField(
            model_name='loader',
            name='pay_method',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pay_methods', to='loaders.paymethod', verbose_name='Метод расчета'),
        ),
    ]
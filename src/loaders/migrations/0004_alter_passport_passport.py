# Generated by Django 3.2.18 on 2023-04-13 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loaders', '0003_auto_20230413_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport',
            name='passport',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='loaders', to='loaders.loader'),
        ),
    ]

# Generated by Django 3.2.18 on 2023-04-14 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loaders', '0006_auto_20230414_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loader',
            name='passport',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='passport', to='loaders.passport'),
        ),
    ]

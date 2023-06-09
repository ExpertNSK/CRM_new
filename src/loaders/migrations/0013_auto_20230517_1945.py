# Generated by Django 3.2.18 on 2023-05-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_alter_client_specialization'),
        ('specializations', '0001_initial'),
        ('loaders', '0012_auto_20230517_1847'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Specialization',
        ),
        migrations.AlterField(
            model_name='loader',
            name='specialization',
            field=models.ManyToManyField(related_name='specializations', to='specializations.Specialization', verbose_name='Специализация'),
        ),
    ]

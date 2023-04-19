from django.db import models

from loaders.models import Loader


class WorkShedule(models.Model):
    loader = models.ForeignKey(
        'loaders.Loader',
        on_delete=models.CASCADE,
    )
    day = models.DateField()
    start_time = models.TimeField(
        null=True,
        blank=True
    )
    end_time = models.TimeField(
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['day']
        unique_together = ('loader', 'day')


class CallResult(models.Model):
    loader = models.OneToOneField(
        Loader,
        on_delete=models.CASCADE,
        verbose_name='Грузчик',
        related_name='calls'
    )
    last_call_result = models.CharField(
        'Статус последнего обзвона',
        max_length=150,
        blank=True,
        null=True
    )
    date_last_call = models.DateField(
        'День последнего обзвона',
        blank=True,
        null=True
    )
    comment = models.TextField(
        'Причина отказа работы',
        blank=True,
        null=True
    )
    day_get_last_status = models.DateField(
        blank=True,
        null=True
    )

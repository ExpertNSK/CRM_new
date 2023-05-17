from django.db import models


class Status(models.Model):
    status = models.CharField(
        verbose_name='Статус',
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.status

from django.db import models

class Specialization(models.Model):
    specialization = models.CharField(
        verbose_name='Тип работы',
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.specialization

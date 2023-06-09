from django.db import models

from specializations.models import Specialization


TYPES_CLIENTS = [
    ('Юридическое лицо', 'Юридическое лицо'),
    ('Физическое лицо', 'Физическое лицо'),
]


class Client(models.Model):
    is_active = models.BooleanField(
        default=True,
    )
    type = models.CharField(
        verbose_name='Тип контрагента',
        choices=TYPES_CLIENTS,
        max_length=16,
    )
    legal_name = models.CharField(
        verbose_name='Юридическое наименование',
        max_length=200,
        unique=True,
    )
    short_name = models.CharField(
        verbose_name='Краткое наименование',
        max_length=100,
        unique=True,
    )
    specialization = models.ManyToManyField(
        Specialization,
        verbose_name='Специализация',
        related_name='clsspecializations'
    )
    inn = models.CharField(
        verbose_name='ИНН',
        max_length=12,
        unique=True,
    )
    kpp = models.CharField(
        verbose_name='КПП',
        max_length=9,
        blank=True,
        null=True,
    )
    legal_address = models.TextField(
        verbose_name='Фактический адрес',
        max_length=200,
        blank=True,
        null=True
    )
    actual_address = models.TextField(
        verbose_name='Фактический адрес',
        max_length=200,
        blank=True,
        null=True,
    )
    payment_account = models.CharField(
        verbose_name='Расчетный счет',
        max_length=20,
        blank=True,
        null=True,
    )
    correspondent_account = models.CharField(
        verbose_name='Корреспондентский счет',
        max_length=20,
        blank=True,
        null=True,
    )
    bik = models.CharField(
        verbose_name='БИК',
        max_length=9,
        blank=True,
        null=True,
    )
    bank = models.CharField(
        verbose_name='Наименование банка',
        max_length=50,
        blank=True,
        null=True,
    )
    

    class Meta:
        ordering = ['short_name']
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'
    
    def __str__(self):
        return f'{self.short_name}'

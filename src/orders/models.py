from django.db import models


STATUSES = [
    ('1', 'Создана'),
    ('1.1', 'Отменена'),
    ('2', 'Расставлено'),
    ('3', 'В работе'),
    ('4', 'Выполнена'),
    ('5', 'Подтверждена'),
    ('6', 'Внутренняя приемка'),
    ('7', 'Закрыта'),
    ('8', 'Включена в счет'),
    ('9', 'Деньги получены'),
]


class Order(models.Model):
    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    status = models.CharField(
        verbose_name='Статус заявки',
        max_length=20,
        choices=STATUSES,
        default='1',
    )
    client = models.ForeignKey(
        'clients.Client',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    description_internal = models.TextField(
        'Внутреннее описание заявки',
        blank=True,
        null=True
    )
    description = models.TextField(
        'Описание заявки для исполнителей',
        blank=True,
        null=True
    )
    

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

from django.db import models


class PaymentType(models.Model):
    payment_type = models.CharField(
        verbose_name='Платежный метод',
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.payment_type


class PayMethod(models.Model):
    payment_type = models.ForeignKey(
        'paymethods.PaymentType',
        on_delete=models.CASCADE,
        related_name='methods',
        verbose_name='Платежный метод',
    )
    requisites = models.CharField(
        verbose_name='Реквизиты оплаты',
        max_length=150,
    )
    bank = models.CharField(
        verbose_name='Наименование банка',
        max_length=150,
    )
    comments = models.TextField(
        verbose_name='Комментарии к оплате',
        max_length=200,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.payment_type}'

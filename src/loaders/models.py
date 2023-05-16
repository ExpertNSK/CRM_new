from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import CustomUser


AREA_OF_RESIDENTS = [
    ('Заельцовский', 'Заельцовский'),
    ('Дзержинский', 'Дзержинский'),
    ('Кировский', 'Кировский'),
    ('Калининский', 'Калининский'),
    ('Ленинский', 'Ленинский'),
    ('Октябрьский', 'Октябрьский'),
    ('Первомайский', 'Первомайский'),
    ('Советский', 'Советский'),
    ('Центральный', 'Центральный '),
    ('НСО', 'НСО')
]

class Loader(models.Model):
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
    )
    middle_name = models.CharField(
        verbose_name='Отчество',
        max_length=150,
    )
    phone = models.CharField(
        verbose_name='Номер телефона',
        max_length=18,
        unique=True,
    )
    whatsapp = models.CharField(
        verbose_name='WhatsApp',
        max_length=18,
        unique=True,
    )
    photo = models.ImageField(
        verbose_name='Фото',
        upload_to='photo/loaders/',
        blank=True
    )
    area = models.CharField(
        verbose_name='Район проживания',
        choices=AREA_OF_RESIDENTS,
        max_length=150,
    )
    specialization = models.ManyToManyField(
        'loaders.Specialization',
        verbose_name='Специализация',
        related_name='specializations',
    )
    status = models.ForeignKey(
        'loaders.Status',
        verbose_name='Статус',
        on_delete=models.PROTECT,
    )
    date_of_employment = models.DateField(
        verbose_name='Дата приема на работу',
        auto_now_add=True,
    )
    first_job_date = models.DateField(
        verbose_name='Дата первой заявки',
        blank=True,
        null=True,
        default=None,
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг',
        validators=[
            MinValueValidator(1, 'Рейтинг не может быть меньше 1!'),
            MaxValueValidator(5, 'Рейтинг не может быть выше 5!')
        ],
        default=5,
    )
    is_active = models.BooleanField(
        default=True,
    )
    referer = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.PROTECT,
        related_name='referer',
        verbose_name='Пригласил',
        blank=True,
        null=True,
    )
    pay_method = models.OneToOneField(
        'paymethods.PayMethod',
        on_delete=models.SET_NULL,
        verbose_name='Метод расчета',
        related_name='pay_methods',
        blank=True,
        null=True,
    )
    passport = models.OneToOneField(
        'passports.Passport',
        on_delete=models.SET_NULL,
        related_name='passport',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Грузчик'
        verbose_name_plural = 'Грузчики'
        ordering = ['last_name']
    
    def __str__(self):
        return (
            f'{self.last_name} {self.first_name} {self.middle_name}'
        )

    def save(self):
        if not CustomUser.objects.filter(phone=self.phone).exists():
            fake_email = f'{self.phone}@email.ru'
            CustomUser.objects.create(
                last_name=self.last_name,
                first_name=self.first_name,
                middle_name=self.middle_name,
                email=fake_email,
                phone=self.phone,
                role='Грузчик',
                password='FaKePaSsWoRd',
            )
        else:
            if (self.referer and self.phone == self.referer.phone):
                raise ValidationError('Реферал не может пригласить сам себя!')
        if not self.whatsapp:
            self.whatsapp = self.phone
        return super(Loader, self).save()


class Status(models.Model):
    status = models.CharField(
        verbose_name='Статус',
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.status


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

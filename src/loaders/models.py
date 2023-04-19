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
        'loaders.PayMethod',
        on_delete=models.SET_NULL,
        verbose_name='Метод расчета',
        related_name='pay_methods',
        blank=True,
        null=True,
    )
    passport = models.OneToOneField(
        'loaders.Passport',
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

class Passport(models.Model):
    serial_number = models.CharField(
        verbose_name='Серия Номер',
        max_length=12,
        unique=True,
    )
    issued_by = models.CharField(
        verbose_name='Кем выдан',
        max_length=200,
    )
    division_code = models.CharField(
        verbose_name='Код подразделения',
        max_length=7,
    )
    date_of_issue = models.DateField(
        verbose_name='Дата выдачи',
    )
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
    birthday = models.DateField(
        verbose_name='День рождения',
    )
    place_of_birth = models.CharField(
        verbose_name='Место рождения',
        max_length=50,
    )
    photo_main_page = models.ImageField(
        verbose_name='Фото главной страницы',
        upload_to='photo/passports/',
        blank=True,
    )
    photo_registration = models.ImageField(
        verbose_name='Фото страницы с пропиской',
        upload_to='photo/passports/',
        blank=True,
    )

    
class PayMethodList(models.Model):
    pay_method = models.CharField(
        verbose_name='Платежный метод',
        max_length=50,
        unique=True,
    )
    
    def __str__(self):
        return self.pay_method


class PayMethod(models.Model):
    pay_method = models.ForeignKey(
        'loaders.PayMethodList',
        on_delete=models.PROTECT,
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

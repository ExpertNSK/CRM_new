from django.db import models


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

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from .managers import CustomUserManager

USER_ROLE_CHOICE = [
    ('Администратор', 'Администратор'),
    ('Руководитель направления', 'Руководитель направления'),
    ('Грузчик', 'Грузчик'),
    ('Директор', 'Директор'),
    ('Диспетчер', 'Диспетчер'),
    ('Менеджер по работе с клиентами', 'Менеджер по работе с клиентами'),
    ('Бухгалтер контролер', 'Бухгалтер контролер'),
    ('Новый пользователь', 'Новый пользователь')
]


class CustomUser(AbstractUser):
    objects = CustomUserManager()
    username = None
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
    email = models.EmailField(
        verbose_name='E-mail',
        max_length=254,
        unique=True,
    )
    phone = models.CharField(
        verbose_name='Номер телефона',
        max_length=18,
        unique=True,
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=30,
        choices=USER_ROLE_CHOICE,
        default='Новый пользователь'
    )
    USERNAME_FIELD = ('phone')
    REQUIRED_FIELDS = [
        'email',
        'last_name',
        'first_name',
        'middle_name'
    ]
    
    @property
    def is_admin(self):
        return (
            self.role == 'Администратор'
            or self.is_superuser
        )
    
    @property
    def is_staff(self):
        return (
            self.role != 'Грузчик'
            or self.role != 'Новый пользователь'
        )
    
    @property
    def is_new(self):
        return (
            self.role == 'Новый пользователь'
        )
    
    class Meta:
        ordering = ['last_name']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self):
        return (
            f'{self.last_name} {self.first_name} {self.middle_name}'
        )
    
    def get_absolute_url(self):
        return reverse('users:edit', kwargs={'id': self.id})
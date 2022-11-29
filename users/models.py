from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def active(self):
        queryset = self.get_queryset().filter(is_active=True)
        queryset.filter(username=None).update(username='Не указано')
        return queryset


class User(AbstractUser):
    objects = UserManager()
    email = models.EmailField(unique=True, verbose_name='эл. почта')
    username = models.CharField(
        'имя пользователя',
        max_length=150,
        blank=True,
        null=True,
        help_text='Не более 150 символов. Буквы, цифры и @/./+/-/_ .',
        validators=[UnicodeUsernameValidator],
        error_messages={
            'unique': 'Пользователь с таким адресом уже существует',
        },
    )
    birthday = models.DateField(
            blank=True,
            null=True,
            verbose_name='день рождения',
    )
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f' {self.email}'

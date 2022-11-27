from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE)
    birthday = models.DateField(
            blank=True,
            null=True,
            verbose_name='день рождения'
        )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    city = models.CharField(max_length=50, verbose_name="Город", help_text="Введите город", **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзеры'
        ordering = ["-date_joined", "-email"]

    def __str__(self):
        return self.email

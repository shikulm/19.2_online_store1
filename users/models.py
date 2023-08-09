from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models.category import NOT_NULLABLE, NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=150, verbose_name='Email', **NOT_NULLABLE, unique=True)
    # first_name = models.CharField(_("first name"), max_length=150, blank=True)
    # last_name = models.CharField(_("last name"), max_length=150, blank=True)
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    key = models.IntegerField(verbose_name='ключ для верификации', **NULLABLE)
    is_active = models.BooleanField(verbose_name='Активный', default=False,
                                    help_text='Поле для активации пользователя', **NOT_NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


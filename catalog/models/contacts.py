from datetime import datetime

from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}
NOT_NULLABLE = {'blank': False, 'null': False}


class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name="имя", **NOT_NULLABLE)
    email = models.EmailField(max_length=254, verbose_name="email", **NOT_NULLABLE)
    message = models.TextField(verbose_name="сообщение", **NULLABLE)

    def __str__(self):
        return f"{self.name} ({self.email})"


    class Meta:
        verbose_name = "контакт"
        verbose_name_plural = "контакты"
        ordering = ('name',)
from datetime import datetime

from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}
NOT_NULLABLE = {'blank': False, 'null': False}


class Category(models.Model):
    name_category = models.CharField(max_length= 150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    # created_at = models.DateTimeField(default=datetime.now, verbose_name='дата создания')


    def __str__(self):
        # return f"{self.name_category} {self.description[:50]}..."
        return f"{self.name_category}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ('name_category',)


class Product(models.Model):
    name_product = models.CharField(max_length=150, verbose_name='наименование', **NOT_NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image_product = models.ImageField(upload_to='products/', verbose_name= 'изображение (превью)', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория', **NOT_NULLABLE)
    price_buy = models.FloatField(default=0, verbose_name='цена за покупку', **NOT_NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', **NOT_NULLABLE)
    changed_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения', **NOT_NULLABLE)

    def __str__(self):
        return f"{self.name_product} {self.price_buy} р. категория ({self.category})"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ('name_product',)


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
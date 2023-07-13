from datetime import datetime

from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


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
    name_product = models.CharField(max_length= 150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image_product = models.ImageField(upload_to='products/', verbose_name= 'изображение (превью)', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price_buy = models.FloatField(default=0, verbose_name='цена за покупку')
    created_at = models.DateTimeField(default=datetime.now, verbose_name='дата создания')
    changed_at = models.DateTimeField(default=datetime.now, verbose_name='дата последнего изменения')

    def __str__(self):
        return f"{self.name_product} {self.price_buy} р. категория ({self.category})"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ('name_product',)



from django.db import models

from catalog.models import Shape
from catalog.models import Product

# Create your models here.
NULLABLE = {'blank': True, 'null': True}
NOT_NULLABLE = {'blank': False, 'null': False}


class Version(models.Model):
    name_version = models.CharField(max_length=150, verbose_name='назание', **NOT_NULLABLE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт', **NULLABLE)
    weight = models.PositiveIntegerField(default=100, verbose_name='вес, гр.', **NOT_NULLABLE)
    shape = models.ForeignKey('Shape', on_delete=models.CASCADE, verbose_name='форма', **NOT_NULLABLE)
    num_version = models.PositiveIntegerField(default=1, verbose_name='номер версии', **NOT_NULLABLE) # Убрать?
    is_actual = models.BooleanField(default=True, verbose_name='доступно для продажи') # Вместо признака текущей версии

    def __str__(self):
        # return f'{self.product} - {self.name_version} ({self.weight} гр, {self.shape})'
        return f'{self.name_version}'

    class Meta:
        verbose_name = "вариант продукта"
        verbose_name_plural = "варианты продуктов"
        ordering = ('name_version',)
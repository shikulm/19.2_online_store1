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


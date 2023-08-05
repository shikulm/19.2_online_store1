from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}
NOT_NULLABLE = {'blank': False, 'null': False}


class Shape(models.Model):
    name_shape = models.CharField(max_length=150, verbose_name='Форма', **NOT_NULLABLE)

    def __str__(self):
        return self.name_shape

    class Meta:
        verbose_name = "форма проудкта"
        verbose_name_plural = "формы продуктов"
        ordering = ('name_shape',)
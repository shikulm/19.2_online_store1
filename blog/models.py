from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}
NOT_NULLABLE = {'blank': False, 'null': False}


class Blog(models.Model):
    caption = models.CharField(max_length=150, verbose_name='заголовок', **NOT_NULLABLE)
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    context_blog = models.TextField(verbose_name='содержимое', **NOT_NULLABLE)
    image_blog = models.ImageField(upload_to='blog/', verbose_name='изображение (превью)', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', **NOT_NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано', **NOT_NULLABLE)
    views_count = models.IntegerField(default=0, verbose_name="просмотры", **NOT_NULLABLE)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'запись блога'
        verbose_name_plural = 'блог'



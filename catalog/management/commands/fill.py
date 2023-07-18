# Заполнение справочников товаров и категорий

from django.core.management import BaseCommand, call_command

from catalog.models import Category, Product


class Command(BaseCommand):


    def handle(self, *args, **options):
        # Удаляем все категории
        Category.objects.all().delete()

        # Удаляем все продукты
        Product.objects.all().delete()

        # Восстанавливаем данные из json файла
        # python manage.py loaddata data.json
        call_command('loaddata', 'data2.json')
        # loaddata data.json
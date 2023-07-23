# Заполнение справочников товаров и категорий

from django.core.management import BaseCommand, call_command

from blog.models import Blog
from catalog.models import Category, Product


class Command(BaseCommand):


    def handle(self, *args, **options):
        # Выгружаем данные в json файла
        call_command('dumpdata', '-o data2.json')
        # python -Xutf8 manage.py dumpdata -o data2.json
        # loaddata data.json
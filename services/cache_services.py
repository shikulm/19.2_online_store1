from blog.models import Blog
from catalog.models import Category
from config.settings import CACHE_ENABLED
from django.conf import settings
from django.core.cache import cache


def get_cache_category():
    # Функция для кэширования категорий
    if CACHE_ENABLED:
        # Проверяем включенность кеша
        key = f'categories_list' # Создаем ключ для хранения
        categories_list = cache.get(key) # Пытаемся получить данные
        if categories_list is None:
            # Если данные не были получены из кеша, то выбираем из БД и записываем в кеш
            categories_list = Category.objects.all()
            cache.set(key, categories_list)
    else:
        # Если кеш не был подключен, то просто обращаемся к БД
        categories_list = Category.objects.all()
    # Возвращаем результат
    return categories_list



def get_cache_blog():
    # Функция для кэширования категорий
    if CACHE_ENABLED:
        # Проверяем включенность кеша
        key = f'blog_list' # Создаем ключ для хранения
        blog_list = cache.get(key) # Пытаемся получить данные
        if blog_list is None:
            # Если данные не были получены из кеша, то выбираем из БД и записываем в кеш
            blog_list = Blog.objects.all()
            cache.set(key, blog_list)
    else:
        # Если кеш не был подключен, то просто обращаемся к БД
        blog_list = Blog.objects.all()
    # Возвращаем результат
    return blog_list
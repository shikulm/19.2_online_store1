"""Создание суперпользователя"""
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = u'Создание суперпользователя'

    def add_arguments(self, parser):
        # Почта
        parser.add_argument('-e', '--email', type=str, help='Почта пользователя', )
        parser.add_argument('-p', '--pass', type=str, help='Пароль пользователя', )
        parser.add_argument('-f', '--firstname', type=str, help='Имя пользователя', )
        parser.add_argument('-l', '--lastname', type=str, help='Фамилия пользователя', )
        parser.add_argument('-a', '--admin', action='store_true', help='Создание учетной записи администратора', )

    def handle(self, *args, **options):
        # Значения по умолчанию
        __mail__ = 'admin@mail.ru'
        __pass__ = 'admin'
        __fn__ =  'admin'
        __ln__ =  'admin'
        __admin__ = False

        if options['email']: __mail__ = options['email']
        if options['pass']: __pass__ = options['pass']
        if options['firstname']: __fn__ = options['firstname']
        if options['lastname']: __ln__ = options['lastname']
        if options['admin']: __admin__ = options['admin']


        user = User.objects.create(
            email=__mail__,
            first_name=__fn__,
            last_name=__ln__,
            is_staff=__admin__,
            is_active=True,
            is_superuser=__admin__
        )

        user.set_password(__pass__)
        user.save()


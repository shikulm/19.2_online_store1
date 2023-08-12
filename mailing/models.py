from django.db import models
from catalog.models.category import NULLABLE, NOT_NULLABLE
# Create your models here.

class Client(models.Model):
    email = models.EmailField(max_length=100, verbose_name='почта', **NOT_NULLABLE)
    first_name = models.CharField(max_length=150, verbose_name='имя', **NOT_NULLABLE)
    last_name = models.CharField(max_length=150, verbose_name='фамилия', **NOT_NULLABLE)
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.last_name} {self.first_name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Message(models.Model):
    subject = models.CharField(max_length=150, verbose_name='тема письма', **NOT_NULLABLE)
    body = models.TextField(verbose_name='содержимое письма', **NOT_NULLABLE)

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'

class MailingSetting(models.Model):

    PERIOD_DAILY = 'day'
    PERIOD_WEEKLY = 'week'
    PERIOD_MONTHLY = 'month'

    PERIODS = ((PERIOD_DAILY, 'раз в день'), (PERIOD_WEEKLY, 'раз в неделю'), (PERIOD_MONTHLY, 'раз в месяц'))

    STATUS_FINISHED = 'finish'
    STATUS_CREATED = 'create'
    STATUS_ACTIVATED = 'active'

    STATUSES = ((STATUS_FINISHED, 'завершена'), (STATUS_CREATED, 'создана'), (STATUS_ACTIVATED, 'запущена'))

    time = models.TimeField(verbose_name='время рассылки', **NOT_NULLABLE)
    period = models.CharField(max_length=150, choices=PERIODS, default=PERIOD_DAILY, verbose_name='период', **NOT_NULLABLE)
    status = models.CharField(max_length=150, choices=STATUSES, default=STATUS_CREATED, verbose_name='статус', **NOT_NULLABLE)

    message = models.ForeignKey(to='Message', on_delete=models.CASCADE, verbose_name='сообщение рассылки', **NOT_NULLABLE)

    def __str__(self):
        return f'{self.time} ({self.period} {self.status})'

    class Meta:
        verbose_name = 'Настройка рассылки'
        verbose_name_plural = 'Настройки рассылки'

class MailingClinet(models.Model):
    mailing = models.ForeignKey('MailingSetting', on_delete=models.CASCADE, verbose_name='рассылка', **NOT_NULLABLE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='клиент', **NOT_NULLABLE)

    def __str__(self):
        return f'{self.mailing} {self.client}'

    class Meta:
        verbose_name = 'Список рассылки'
        verbose_name_plural = 'Списки рассылок'


class MailingLog(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAIL = 'fail'
    STATUSES = ((STATUS_OK, 'Успешно'),(STATUS_FAIL, 'Ошибка'))

    datetime_mailing = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки', **NOT_NULLABLE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='клиент', **NOT_NULLABLE)
    setting = models.ForeignKey('MailingSetting', on_delete=models.CASCADE, verbose_name='настройки', **NOT_NULLABLE)
    status = models.CharField(max_length=150, verbose_name='статус', choices=STATUSES, default=STATUS_OK, **NOT_NULLABLE)
    answer = models.TextField(verbose_name='ответ почтового сервера', **NULLABLE)


    def __str__(self):
        return f'{self.datetime_mailing} {self.client} {self.setting} {self.status}'

    class Meta:
        verbose_name = 'Запись журнала рассылки'
        verbose_name_plural = 'Журнал рассылок'


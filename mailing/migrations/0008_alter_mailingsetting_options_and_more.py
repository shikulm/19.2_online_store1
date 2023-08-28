# Generated by Django 4.2.3 on 2023-08-24 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0007_client_owner_mailingsetting_owner_message_owner_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailingsetting',
            options={'ordering': ('datestart', 'message'), 'permissions': [('set_status', 'Can disable mailing')], 'verbose_name': 'Настройка рассылки', 'verbose_name_plural': 'Настройки рассылки'},
        ),
        migrations.AlterField(
            model_name='mailingsetting',
            name='dateend',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 31, 11, 24, 5, 444864, tzinfo=datetime.timezone.utc), null=True, verbose_name='дата окончания'),
        ),
        migrations.AlterField(
            model_name='mailingsetting',
            name='datestart',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 24, 11, 24, 5, 444849, tzinfo=datetime.timezone.utc), null=True, verbose_name='дата начала'),
        ),
    ]
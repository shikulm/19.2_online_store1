# Generated by Django 4.2.3 on 2023-08-08 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Поле для активации пользователя', verbose_name='Активный'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-14 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingsetting',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='время рассылки'),
        ),
    ]

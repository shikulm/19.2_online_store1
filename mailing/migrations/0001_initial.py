# Generated by Django 4.2.3 on 2023-08-12 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='почта')),
                ('first_name', models.CharField(max_length=150, verbose_name='имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='фамилия')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150, verbose_name='тема письма')),
                ('body', models.TextField(verbose_name='содержимое письма')),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письма',
            },
        ),
        migrations.CreateModel(
            name='MailingSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='время рассылки')),
                ('period', models.CharField(choices=[('day', 'раз в день'), ('week', 'раз в неделю'), ('month', 'раз в месяц')], default='day', max_length=150, verbose_name='период')),
                ('status', models.CharField(choices=[('finish', 'завершена'), ('create', 'создана'), ('active', 'запущена')], default='create', max_length=150, verbose_name='статус')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.message', verbose_name='сообщение рассылки')),
            ],
            options={
                'verbose_name': 'Настройка рассылки',
                'verbose_name_plural': 'Настройки рассылки',
            },
        ),
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_mailing', models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки')),
                ('status', models.CharField(choices=[('ok', 'Успешно'), ('fail', 'Ошибка')], default='ok', max_length=150, verbose_name='статус')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='ответ почтового сервера')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.client', verbose_name='клиент')),
                ('setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingsetting', verbose_name='настройки')),
            ],
            options={
                'verbose_name': 'Запись журнала рассылки',
                'verbose_name_plural': 'Журнал рассылок',
            },
        ),
        migrations.CreateModel(
            name='MailingClinet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.client', verbose_name='клиент')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingsetting', verbose_name='рассылка')),
            ],
            options={
                'verbose_name': 'Список рассылки',
                'verbose_name_plural': 'Списки рассылок',
            },
        ),
    ]

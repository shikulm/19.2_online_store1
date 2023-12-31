# Generated by Django 4.2.3 on 2023-08-04 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_product_changed_at_alter_product_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_shape', models.CharField(max_length=150, verbose_name='Форма')),
            ],
            options={
                'verbose_name': 'форма',
                'verbose_name_plural': 'формы',
                'ordering': ('name_shape',),
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_version', models.CharField(max_length=150, verbose_name='Форма')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='вес, гр.')),
                ('num_version', models.PositiveIntegerField(default=1, verbose_name='номер версии')),
                ('is_actual', models.BooleanField(default=True, verbose_name='актуально для продажи')),
                ('shape', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.shape', verbose_name='форма')),
            ],
            options={
                'verbose_name': 'вариант',
                'verbose_name_plural': 'варианты',
                'ordering': ('name_version',),
            },
        ),
    ]

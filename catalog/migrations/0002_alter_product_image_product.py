# Generated by Django 4.2.3 on 2023-07-13 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_product',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='изображение (превью)'),
        ),
    ]

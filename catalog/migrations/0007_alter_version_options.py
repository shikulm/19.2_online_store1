# Generated by Django 4.2.3 on 2023-08-04 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_shape_options_version_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'ordering': ('name_version',), 'verbose_name': 'вариант продукта', 'verbose_name_plural': 'варианты продуктов'},
        ),
    ]

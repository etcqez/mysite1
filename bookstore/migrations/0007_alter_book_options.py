# Generated by Django 4.2 on 2023-05-16 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0006_book_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '图书', 'verbose_name_plural': '图书'},
        ),
    ]

# Generated by Django 3.2.16 on 2022-11-28 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221128_2042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
    ]

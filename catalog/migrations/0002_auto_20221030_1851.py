# Generated by Django 3.2.16 on 2022-10-30 15:51

import catalog.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'тег', 'verbose_name_plural': 'теги'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='tag',
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(to='catalog.Tag', verbose_name='теги'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='max 150 символов', max_length=150, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='category',
            name='weight',
            field=models.PositiveSmallIntegerField(default=100, verbose_name='вес категории'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(help_text='Выберите категорию', on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(help_text='max 150 символов', max_length=150, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(help_text='Описание должно быть больше чем из 2-ух слов                                       и содержать слова "превосходно" и "роскошно".', validators=[catalog.validators.item_text_validator], verbose_name='текст'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(help_text='max 150 символов', max_length=150, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(verbose_name='Ссылка'),
        ),
    ]

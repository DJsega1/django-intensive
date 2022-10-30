from django.db import models
from Core.models import NamedBaseModel, PublishableBaseModel, SlugBaseModel
from .validators import item_text_validator


class Tag(PublishableBaseModel, NamedBaseModel, SlugBaseModel):
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self) -> str:
        return self.name


class Category(PublishableBaseModel, NamedBaseModel, SlugBaseModel):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
    weight = models.PositiveSmallIntegerField(default=100, verbose_name='вес категории')

    def __str__(self) -> str:
        return self.name


class Item(PublishableBaseModel, NamedBaseModel):
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория',
                                 help_text='Выберите категорию')
    tags = models.ManyToManyField(Tag, verbose_name='теги')
    text = models.TextField(verbose_name='текст',
                            help_text=('Описание должно быть больше чем из 2-ух слов'
                                       'и содержать слова "превосходно" и "роскошно".'),
                            validators=[item_text_validator('превосходно', 'роскошно')])

    def __str__(self) -> str:
        return self.name

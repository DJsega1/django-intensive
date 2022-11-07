from django.db import models
from sorl.thumbnail import get_thumbnail
from Core.models import NamedBaseModel, PublishableBaseModel, SlugBaseModel, ImageBaseModel
from .validators import item_text_validator


class Tag(PublishableBaseModel, NamedBaseModel, SlugBaseModel):
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self) -> str:
        return self.name


class Category(PublishableBaseModel, NamedBaseModel, SlugBaseModel):
    weight = models.PositiveSmallIntegerField(default=100, verbose_name='вес категории')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self) -> str:
        return self.name


class Item(PublishableBaseModel, NamedBaseModel, ImageBaseModel):
    tags = models.ManyToManyField(Tag, verbose_name='теги')
    text = models.TextField(verbose_name='текст',
                            help_text=('Описание должно быть больше чем из 2-ух слов'
                                       'и содержать слова "превосходно" и "роскошно".'),
                            validators=[item_text_validator('превосходно', 'роскошно')])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория',
                                 help_text='Выберите категорию')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self) -> str:
        return self.name


class Image(ImageBaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='товар', default=1)

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'

    def __str__(self) -> str:
        return f'Изображение товара {self.item}'

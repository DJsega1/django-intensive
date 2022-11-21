from django.db import models
from ckeditor.fields import RichTextField

from Core.models import NamedBaseModel, PublishableBaseModel, \
                        SlugBaseModel, ImageBaseModel
from catalog.validators import item_text_validator


class Tag(PublishableBaseModel, NamedBaseModel, SlugBaseModel):
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self) -> str:
        return self.name


class Category(PublishableBaseModel, NamedBaseModel, SlugBaseModel):
    weight = models.PositiveSmallIntegerField(
            default=100,
            verbose_name='вес категории'
            )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self) -> str:
        return self.name


class ItemManager(models.Manager):
    def published(self):
        return (self.get_queryset()
                .filter(is_published=True)
                .select_related('preview')
                .select_related('category')
                .order_by('category__name', 'name')
                .prefetch_related('tags')
                )


class Item(PublishableBaseModel, NamedBaseModel):
    objects = ItemManager()
    tags = models.ManyToManyField(Tag, verbose_name='теги')
    text = RichTextField(
        verbose_name='текст',
        help_text=('описание должно быть больше чем из 2-ух'
                   ' слов и содержать слова "превосходно"'
                   ' и "роскошно".'),
        validators=[
            item_text_validator('превосходно', 'роскошно')
        ]
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='категория',
                                 help_text='выберите категорию')
    is_on_main = models.BooleanField(default=False, verbose_name='на главной')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def preview_tmb(self):
        return Preview.objects.get(item=self.pk).image_tmb()

    def __str__(self) -> str:
        return self.name

    preview_tmb.allow_tags = True
    preview_tmb.short_description = 'превью'


class Preview(ImageBaseModel):
    item = models.OneToOneField(Item, on_delete=models.CASCADE,
                                verbose_name='товар', default=1)

    class Meta:
        verbose_name = 'превью'
        verbose_name_plural = 'превью'

    def __str__(self) -> str:
        return f'превью товара {self.item}'


class Gallery(ImageBaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             verbose_name='товар', default=1)

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'галерея'

    def __str__(self) -> str:
        return f'изображение товара {self.item}'

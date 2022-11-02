from django.db import models


class PublishableBaseModel(models.Model):
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        abstract = True
        verbose_name = 'Публикуемый объект'


class NamedBaseModel(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название", help_text="max 150 символов")

    class Meta:
        abstract = True
        verbose_name = 'Именованный объект'


class SlugBaseModel(models.Model):
    slug = models.SlugField(verbose_name="Ссылка")

    class Meta:
        abstract = True
        verbose_name = 'Ссылающийся объект'

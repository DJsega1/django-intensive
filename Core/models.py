from django.db import models


class PublishableBaseModel(models.Model):
    class Meta:
        abstract = True
        verbose_name = 'Публикуемый объект'
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")


class NamedBaseModel(models.Model):
    class Meta:
        abstract = True
        verbose_name = 'Именованный объект'
    name = models.CharField(max_length=150, verbose_name="Название", help_text="max 150 символов")


class SlugBaseModel(models.Model):
    class Meta:
        abstract = True
        verbose_name = 'Ссылающийся объект'
    slug = models.SlugField(verbose_name="Ссылка")

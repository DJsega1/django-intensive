from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail


class PublishableBaseModel(models.Model):
    is_published = models.BooleanField(default=True, 
                                       verbose_name="Опубликовано")

    class Meta:
        abstract = True
        verbose_name = 'Публикуемый объект'


class NamedBaseModel(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название",
                            help_text="max 150 символов")

    class Meta:
        abstract = True
        verbose_name = 'Именованный объект'


class SlugBaseModel(models.Model):
    slug = models.SlugField(verbose_name="Ссылка")

    class Meta:
        abstract = True
        verbose_name = 'Ссылающийся объект'


class ImageBaseModel(models.Model):
    upload = models.ImageField(
            upload_to='uploads/%Y/%m', 
            default='default.jpg', 
            verbose_name='изображение'
        )

    class Meta:
        abstract = True
        verbose_name = 'Объект-изображение'

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300',
                             crop='center', quality=51)

    def image_tmb(self):
        if self.upload:
            return mark_safe(f'<img src="{self.get_img.url}">')
        return 'No image'

    image_tmb.short_description = 'изображение'
    image_tmb.allow_tags = True

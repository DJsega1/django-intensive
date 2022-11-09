from django.contrib import admin
from .models import Tag, Category, Item, Preview, Gallery
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe


class GalleryImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" width="150" height="150"  style="object-fit: cover;"/></a> %s ' % \
                (image_url, image_url, file_name, _('')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class PreviewInline(admin.TabularInline):
    model = Preview
    fk_name = "item"
    readonly_fields = ('image_tmb',)


class GalleryInline(admin.TabularInline):
    model = Gallery
    fk_name = "item"
    readonly_fields = ('image_tmb',)


@admin.register(Item)
class ItemModelAdmin(admin.ModelAdmin):
    inlines = [
        PreviewInline, GalleryInline
    ]
    list_display = ('name', 'is_published', 'image_tmb',)
    list_editable = ('is_published',)
    list_display_links = ('name',)
    filter_horizontal = ('tags',)


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Preview)
class PreviewModelAdmin(admin.ModelAdmin):
    list_display = ('image_tmb', 'item',)
    list_display_links = ('image_tmb',)


@admin.register(Gallery)
class GalleryModelAdmin(admin.ModelAdmin):
    list_display = ('image_tmb', 'item',)
    list_display_links = ('image_tmb',)

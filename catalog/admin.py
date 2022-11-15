from django.contrib import admin
from .models import Tag, Category, Item, Preview, Gallery


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
    list_display = ('name', 'is_published', 'preview_tmb',)
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

from django.contrib import admin
from .models import Tag, Category, Item, Image


@admin.register(Item)
class ItemModelAdmin(admin.ModelAdmin):
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


@admin.register(Image)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('image_tmb', 'item',)
    list_display_links = ('image_tmb',)

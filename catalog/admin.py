from django.contrib import admin
from .models import Tag, Category, Item


class ItemModelAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published",)
    list_editable = ("is_published",)
    list_display_links = ("name",)
    filter_horizontal = ("tags",)


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Item, ItemModelAdmin)

from django.shortcuts import render
from catalog.models import Item


def home(request):
    template = 'homepage/index.html'
    MAX_TEXT_WORDS = 10
    items = Item.objects.published().filter(is_on_main=True)
    context = {
        'MAX_TEXT_WORDS': MAX_TEXT_WORDS,
        'items': items
    }
    return render(request, template, context)

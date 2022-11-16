from django.shortcuts import render, get_object_or_404
from .models import Item


def item_list(request):
    template = 'catalog/list.html'
    items = Item.objects.all().order_by('category')
    context = {
        'items': items,
    }
    return render(request, template, context)


def item_detail(request, pk):
    template = 'catalog/detail.html'
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item': item,
    }
    return render(request, template, context)

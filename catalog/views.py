from django.shortcuts import render


def item_list(request):
    context = {}
    return render(request, "catalog/index.html", context)


def item_detail(request, pk):
    context = {}
    return render(request, "catalog/index.html", context)

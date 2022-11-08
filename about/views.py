from django.shortcuts import render


def description(request):
    context = {}
    return render(request, "about/index.html", context)

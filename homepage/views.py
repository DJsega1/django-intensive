from django.http import HttpResponse


def home(request):
    return HttpResponse('<img src="https://www.pinclipart.com/picdir/big/571-5719247_trans\
                         parent-pusheen-clip-art-pusheen-cat-gif-png.png" alt="Главная">')

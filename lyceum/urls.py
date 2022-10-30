from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homepage.urls', namespace='homepage')),
    path('about/', include('about.urls', namespace='about')),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('admin/', admin.site.urls),
]

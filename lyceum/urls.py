from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('homepage.urls', namespace='homepage')),
    path('about/', include('about.urls', namespace='about')),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('feedback/', include('feedback.urls', namespace='feedback')),
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(
                settings.MEDIA_URL,
                document_root=settings.MEDIA_ROOT
            )
        urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls'))
    ]

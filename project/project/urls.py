from django.contrib import admin
import django.urls
import django.conf.urls.static

urlpatterns = [
    django.urls.path('admin/', admin.site.urls),
    django.urls.path('users/', django.urls.include('users.urls')),
    django.urls.path('workers/', django.urls.include('workers.urls')),
]

urlpatterns += django.conf.urls.static.static(
    django.conf.settings.MEDIA_URL,
    document_root=django.conf.settings.MEDIA_ROOT,
)

urlpatterns += django.conf.urls.static.static(
    django.conf.settings.STATIC_URL,
    document_root=django.conf.settings.STATIC_ROOT,
)
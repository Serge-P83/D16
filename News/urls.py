from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('portal_news.urls')),
    path('', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
]

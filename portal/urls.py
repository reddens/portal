from accounts import urls
from django import urls
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('prospects/', include('prospects.urls'))
]

urlpatterns += staticfiles_urlpatterns()

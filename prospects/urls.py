from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

app_name = "prospects"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('create', views.apply, name="apply"),
    url(r'^(?P<slug>[\w-]+)/$', views.view_student, name="view")
]
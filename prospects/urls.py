from django.contrib import admin
from django.urls import path
from . import views

app_name = "prospects"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('create', views.apply, name="apply"),
]
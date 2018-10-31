from django.urls import path
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    ]
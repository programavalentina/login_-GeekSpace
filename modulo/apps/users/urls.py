from django.urls import path
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register', views.RegistroUsuario.as_view()),
    path('profile', views.profile, name='profile'),
    ]
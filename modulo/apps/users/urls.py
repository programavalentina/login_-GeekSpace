from django.urls import path
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.RegistroUsuario.as_view()),
    path('profile', login_required(views.profile, 'modulo:index', '/users/login') , name='profile'),
    path('logout', LogoutView.as_view(template_name='modulo/index.html'), name='logout'),
    ]
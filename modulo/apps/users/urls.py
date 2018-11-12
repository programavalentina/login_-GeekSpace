from django.urls import path
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.RegistroUsuario.as_view(), name='register'),
    path('profile', login_required(views.profile, 'modulo:index', '/users/login') , name='profile'),
    path('logout', LogoutView.as_view(template_name='modulo/index.html'), name='logout'),
    path('courses',  login_required(views.courses, 'modulo:index', '/users/login') , name='courses'),
    path('create-course', login_required(views.CreateCourse.as_view(), 'modulo:index', '/users/login') , name ='create-course'),
    path('update-course/<int:pk>/',login_required(views.UpdateCourse.as_view(), 'modulo:index', '/users/login')  , name='update-course'),
    path('delete-course/<int:pk>/', login_required(views.DeleteCourse.as_view(), 'modulo:index', '/users/login') , name='delete-course'),
    path('users', login_required(views.users,'modulo:index', '/users/login'),  name='users'),
    path('create-user', login_required(views.CreateUser.as_view(), 'modulo:index', '/users/login') , name='create-course'),
    path('update-user/<int:pk>/', login_required(views.UpdateUser.as_view(), 'modulo:index', '/users/login') , name='update-course'),
    path('delete-user/<int:pk>/', login_required(views.DeleteUser.as_view(), 'modulo:index', '/users/login') , name='delete-course'),
    ]



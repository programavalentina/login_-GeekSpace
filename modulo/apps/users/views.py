from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .backends import UserAuth
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import *
from .models import *
# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = "users/register.html"
    form_class = UserForm
    success_url = reverse_lazy("modulo:index")

def login(request):
    return render(request, 'users/login.html')

def profile(request):
    return render(request, 'users/profile.html')

def login(request):
    error = 0
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print('entro')
            username = request.POST['username']
            password = request.POST['password']
            auth_ = UserAuth()
            user = auth_.authenticate(username=username, password=password)
            if user is not None:
                print("existe")
                auth.login(request, user)
                return redirect('users:profile')
            else:
                return render(request, 'users/login.html', {'form':form, 'error':error})
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form, 'error':error})

def courses(request):
    courses = Course.objects.all()
    return render(request, 'users/courses.html', {'courses':courses})

class CreateCourse(CreateView):
    model= Course
    template_name = 'users/create_course.html'
    form_class = CourseForm
    success_url = reverse_lazy('users:courses')

class UpdateCourse(UpdateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('users:courses')
    template_name = 'users/update_course.html'

class DeleteCourse(DeleteView):
    model = Course
    success_url = reverse_lazy('users:courses')
    template_name = 'users/delete_course.html'

def users(request):
    users = User.objects.all()
    return render(request, 'users/users.html', {'users':users})

class CreateUser(CreateView):
    model= User
    template_name = 'users/create_user.html'
    form_class = UserForm
    success_url = reverse_lazy('users:users')

class UpdateUser(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:users')
    template_name = 'users/update_user.html'

class DeleteUser(DeleteView):
    model = User
    success_url = reverse_lazy('users:users')
    template_name = 'users/delete_user.html'
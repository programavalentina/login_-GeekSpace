from django.shortcuts import render, redirect
from django.http import  HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .backends import UserAuth
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserForm, LoginForm
from django.contrib.auth.views import LoginView, LogoutView
import logging
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


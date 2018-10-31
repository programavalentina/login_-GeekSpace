from django.shortcuts import render
from django.http import  HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserForm
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
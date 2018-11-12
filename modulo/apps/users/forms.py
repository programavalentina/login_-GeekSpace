from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets, forms

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'Name1',
            'Name2',
            'Name3',
            'LastName1',
            'LastName2',
            'BirthDate',
            'Email',
            'Phone',
            'FKLicenceType',
        ]
        labels = {
            'username':'Username',
            'Name1':'Name1',
            'Name2': 'Name2',
            'Name3': 'Name3',
            'LastName1': 'LastName',
            'LastName2': 'LastName2',
            'BirthDate': 'BirthDate',
            'Email': 'Email',
            'Phone': 'Phone',
            'FKLicenceType':'FKLicenceType',
        }
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'Name1': widgets.TextInput(attrs={'class': 'form-control'}),
            'Name2': widgets.TextInput(attrs={'class': 'form-control'}),
            'Name3': widgets.TextInput(attrs={'class': 'form-control'}),
            'LastName1': widgets.TextInput(attrs={'class': 'form-control'}),
            'LastName2': widgets.TextInput(attrs={'class': 'form-control'}),
            'Email': widgets.TextInput(attrs={'class': 'form-control'}),
            'Phone': widgets.TextInput(attrs={'class': 'form-control'}),
            'BirthDate': widgets.DateTimeInput(attrs={'class': 'form-control'}),
        }

class LoginForm(forms.Form):
    username = forms.Field(widget=widgets.TextInput(attrs={'class':'form-control'}))
    password = forms.Field(widget=widgets.PasswordInput(attrs={'class':'form-control'}))
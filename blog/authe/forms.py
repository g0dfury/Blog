from django import forms # importing forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class UserSignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'


    class Meta: 
        model = User
        fields = ('username','email', 'full_name', 'password1', 'password2')

        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Введите email'}),
            'full_name': forms.TextInput(attrs={'placeholder': 'Введите полное имя'}),
            'username': forms.TextInput(attrs={'placeholder':'Введите имя пользователя'})
            }


class UserSignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))



from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy

from blog_app import urls
from .forms import UserSignUpForm, UserSignInForm
from .models import User

class Register(View): # для регистрации
    def get(self, request):
        form = UserSignUpForm()
        context = {'form': form}
        return render(request, 'authe/register.html', context=context)

    def post(self, request):
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('authe:login'))
        else:
            context = {'form': form}
            return render(request, 'authe/register.html', context=context)


class Login(View): # для логина
    def get(self, request):
        form = UserSignInForm()
        context = {'form':form}
        return render(request, 'authe/login.html', context=context)

    def post(self, request):
        form = UserSignInForm(request, request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy('blogs:index'))
        
        return render(request, 'authe/fail.html', context={'form': form})


class Index(View):
    def get(self, request):
        return render(request, 'authe/index.html')

class Fail(View):
    def get(self, request):
        return render(request, 'authe/fail.html')
    
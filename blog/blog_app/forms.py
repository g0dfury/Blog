from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Введите заголовок блога'}),
            'content': forms.Textarea(attrs={'placeholder':'Введите описание блога'})
        }
        


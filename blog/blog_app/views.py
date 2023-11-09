from django.shortcuts import render
from django.views import View # importing View
from .models import Blog # importing our models
from django.http import HttpResponse # importing HttpResponse

class ViewAllBlogs(View):
    def get(self, request):
        blogs = Blog.objects.all()
        context = {
            'title': 'Список блогов',
            'blogs': blogs,
        }

        return render(request, 'blog_app/index.html', context=context)


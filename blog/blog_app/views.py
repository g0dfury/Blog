from django.shortcuts import render, redirect
from django.views import View # importing View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Blog # importing our models
from .forms import BlogForm

class ViewAllBlogs(View):
    def get(self, request):
        blogs = Blog.objects.all()
        context = {
            'title': 'Список блогов',
            'blogs': blogs,
        }

        return render(request, 'blog_app/index.html', context=context)


class CreateBlogView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = BlogForm()
        context = {'form': form}
        return render(request, 'blog_app/create.html', context=context)

    @method_decorator(login_required)
    def post(self, request):
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # Устанавливаем автора как текущего пользователя
            blog.save()
            return redirect('blogs:index')
        return render(request, 'blog_app/create.html', {'form': form})
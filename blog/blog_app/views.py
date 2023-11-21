from django.shortcuts import render, redirect
from django.views import View # importing View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

from .models import Blog # importing our models
from .forms import BlogForm
from authe.models import User

class ViewAllBlogs(View):   # главная
    def get(self, request):
        blogs = Blog.objects.all()
        context = {
            'title': 'Список блогов',
            'blogs': blogs,
        }

        return render(request, 'blog_app/index.html', context=context)


class CreateBlogView(View):     # создать
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
    


class ProfileView(View):        # личный профиль
    def get(self, request):
        user = request.user
        blogs = Blog.objects.filter(author=user)

        context = {
            'title': 'Мой профиль',
            'user': user,
            'blogs': blogs,
        }
        
        return render(request, 'blog_app/profile.html', context=context)
    

# class EditBlogView(View):   # edit
#     def get(self, request, blog_id):
#         blog = Blog.objects.get(id = blog_id)
#         form = BlogForm()
#         context = {
#             'title':'Редактировать блог',
#             'blog': blog,
#             'form': form
#         }

#         return render(request, 'blog_app/edit.html', context=context)
    
#     def post(self, request, blog_id):
#         blog = Blog.objects.get(id=blog_id)
#         form = BlogForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('blog_app/profile.html')
#         return render(request, 'blog_app/edit.html', context = {'form':form, 'blog': blog})
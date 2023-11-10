from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.ViewAllBlogs.as_view(), name='index'),
    path('create', views.CreateBlogView.as_view(), name='create'),
]


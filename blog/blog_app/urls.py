from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.ViewAllBlogs.as_view(), name='index'),
    path('create/', views.CreateBlogView.as_view(), name='create'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('edit/<int:blog_id>/', views.EditBlog.as_view(), name='edit'),
    path('delete/<int:blog_id>/', views.DeleteBlog.as_view(), name='delete'),
]


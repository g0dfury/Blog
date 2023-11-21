from django.urls import path
from .views import Register, Login, Index, Fail, signout
from . import views

app_name = 'authe'

urlpatterns = [
    path('', Register.as_view(), name = 'register'),
    path('login/', Login.as_view(), name='login'),
    path('', Index.as_view(), name='index'),
    path('fail/', Fail.as_view(), name='fail'),
    path('signout/', signout, name='signout'),
]
from django.urls import path

from . import login,isLogin

urlpatterns = [
    path('login/', login.login),
    path('isLogin/', isLogin.isLogin),
]
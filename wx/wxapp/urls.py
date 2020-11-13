from django.urls import path

from . import views,login,changeUserInfo,getUserInfo

urlpatterns = [
    path('login/', login.login),
    path('changeUserInfo/', changeUserInfo.changeUserInfo),
    path('getUserInfo/', getUserInfo.getUserInfo),
]
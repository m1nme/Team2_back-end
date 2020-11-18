from django.urls import path

from . import views,login,changeUserInfo,getUserInfo,addCat,getCatInfo,showCatsList,feedCat

urlpatterns = [
    path('login/', login.login),
    path('changeUserInfo/', changeUserInfo.changeUserInfo),
    path('getUserInfo/', getUserInfo.getUserInfo),
    path('addCat/', addCat.addCat),
    path('getCatInfo/', getCatInfo.getCatInfo),
    path('showCatsList/', showCatsList.showCatsList),
    path('feedCat/', feedCat.feedCat),
]
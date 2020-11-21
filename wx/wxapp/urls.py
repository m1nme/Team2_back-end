from django.urls import path

from . import views,login,changeUserInfo,getUserInfo,addCat,getCatInfo,showCatsList,feedCat
from . import getFeedLog
from .import uploadImg
urlpatterns = [
    path('login/', login.login),
    path('changeUserInfo/', changeUserInfo.changeUserInfo),
    path('getUserInfo/', getUserInfo.getUserInfo),
    path('addCat/', addCat.addCat),
    path('getCatInfo/', getCatInfo.getCatInfo),
    path('showCatsList/', showCatsList.showCatsList),
    path('feedCat/', feedCat.feedCat),
    path('getFeedLog/', getFeedLog.getFeedLog),
    path('uploadImg/', uploadImg.uploadImg),
]
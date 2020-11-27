from django.urls import path

from . import login,isLogin
from . import showCats,getCatInfo,modifyCatInfo
from . import showPosts,getPostInfo,modifyPostInfo
from . import showComments,getCommentInfo,modifyCommentInfo
from . import showFeedbacks,getFeedbackInfo,modifyFeedbackInfo
urlpatterns = [
    path('login/', login.login),
    path('isLogin/', isLogin.isLogin),

    path('showCats/', showCats.showCats),
    path('getCatInfo/', getCatInfo.getCatInfo),
    path('modifyCatInfo/', modifyCatInfo.modifyCatInfo),

    path('showPosts/', showPosts.showPosts),
    path('getPostInfo/', getPostInfo.getPostInfo),
    path('modifyPostInfo/', modifyPostInfo.modifyPostInfo),

    path('showComments/', showComments.showComments),
    path('getCommentInfo/', getCommentInfo.getCommentInfo),
    path('modifyCommentInfo/', modifyCommentInfo.modifyCommentInfo),

    path('showFeedbacks/', showFeedbacks.showFeedbacks),
    path('getFeedbackInfo/', getFeedbackInfo.getFeedbackInfo),
    path('modifyFeedbackInfo/', modifyFeedbackInfo.modifyFeedbackInfo),
]
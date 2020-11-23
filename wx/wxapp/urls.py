from django.urls import path

from . import login,changeUserInfo,getUserInfo
from . import addCat,getCatInfo,showCatsList
from . import getFeedLog,deleteFeedLog,modifyFeedLog,feedCat
from .import uploadImg
from . import publishPost,getPostInfo,deletePost,showPostsLog
from . import publishComment,showComments,deleteComment,showCommentsLog
from . import submitFeedback,showFeedbacksList,getFeedbackInfo
from . import like,showLikesLog,getLikesNum
urlpatterns = [
    path('login/', login.login),
    path('changeUserInfo/', changeUserInfo.changeUserInfo),
    path('getUserInfo/', getUserInfo.getUserInfo),
    
    path('addCat/', addCat.addCat),
    path('getCatInfo/', getCatInfo.getCatInfo),
    path('showCatsList/', showCatsList.showCatsList),
    
    path('feedCat/', feedCat.feedCat),
    path('getFeedLog/', getFeedLog.getFeedLog),
    path('deleteFeedLog/', deleteFeedLog.deleteFeedLog),
    path('modifyFeedLog/', modifyFeedLog.modifyFeedLog),

    path('uploadImg/', uploadImg.uploadImg),

    path('publishPost/', publishPost.publishPost),
    path('deletePost/', deletePost.deletePost),
    path('getPostInfo/', getPostInfo.getPostInfo),
    path('showPostsLog/', showPostsLog.showPostsLog),

    path('publishComment/', publishComment.publishComment),
    path('showComments/', showComments.showComments),
    path('deleteComment/', deleteComment.deleteComment),
    path('showCommentsLog/', showCommentsLog.showCommentsLog),

    path('submitFeedback/', submitFeedback.submitFeedback),
    path('showFeedbacksList/', showFeedbacksList.showFeedbacksList),
    path('getFeedbackInfo/', getFeedbackInfo.getFeedbackInfo),

    path('like/', like.like),
    path('showLikesLog/', showLikesLog.showLikesLog),
    path('getLikesNum/', getLikesNum.getLikesNum),
]
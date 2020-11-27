from django.http import JsonResponse
from wx.ret import ret
import json
from wxapp import models
from manager.verifyToken import verifyToken
from django.core.paginator import Paginator, EmptyPage

def getPostInfo(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        postid = params['postId']

        result = verifyToken(token)
        if(result==True):
            try:
                post = models.posts.objects.get(id=postid)
                response = JsonResponse({"error_code": 0, "msg": "success", "data": {
                                                                                    "postId": post.id,
                                                                                    "postTitle": post.title,
                                                                                    "postContent": post.content,
                                                                                    "urlList": post.urllist,
                                                                                    "catId": post.catid,
                                                                                    "username": post.username,
                                                                                    "postTime": post.modifytime,
                                                                                    "postVet": post.vet
                                                                                    }})
                return ret(response)
            except:
                response = JsonResponse({"error_code": 1, "msg": "ID error"})
                return ret(response)
        else:
            response = JsonResponse({"error_code": 1, "msg": result})
            return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
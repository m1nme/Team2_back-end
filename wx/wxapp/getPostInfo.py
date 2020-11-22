from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def getPostInfo(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        postid = params['postId']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        try:
            post = models.posts.objects.get(id=postid,vet=1)
            response = JsonResponse({
                                    "error_code": 0,
                                    "msg": "success",
                                    "data": {
                                        "title": post.title,
                                        "content": post.content,
                                        "urlList": post.urllist,
                                        "userName": post.username,
                                        "userUrl": post.userurl,
                                        "catId": post.catid,
                                        "time": post.modifytime
                                        }
                                    })
            return ret(response)
        except:
            response = JsonResponse({"error_code": 1, "msg": "postId error"})
            return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
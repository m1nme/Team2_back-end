from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def deletePost(request):
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
            post = models.posts.objects.get(openid=openid,id=postid)
            post.delete()
            response = JsonResponse({"error_code": 0, "msg": "success"})
            return ret(response)
        except:
            response = JsonResponse({"error_code": 1, "msg": "postId error"})
            return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
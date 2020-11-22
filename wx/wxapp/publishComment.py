from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def publishComment(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        
        try:
            postid = params['postId']
            content = params['content']
            if(len(content)>300):
                response = JsonResponse({"error_code": 0, "msg": "something too long"})
                return ret(response)                
            user = models.user.objects.get(openid=openid)
            username = user.nickname
            userurl =  user.url

            models.comments.objects.create(postid=postid,
                                        content=content,
                                        openid=openid,
                                        username=username,
                                        userurl=userurl,
                                        vet=0)
            response = JsonResponse({"error_code": 0, "msg": "success"})
            return ret(response)
        except:
            response = JsonResponse({"error_code": 1, "msg": "params error"})
            return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
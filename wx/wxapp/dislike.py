from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def dislike(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        ID = params['ID']
        TYPE = params['TYPE']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        if(TYPE=='CAT'):
            try:
                res = models.likecats.objects.get(openid=openid,catid=ID)
                res.delete()
                response = JsonResponse({"error_code": 0, "msg": "success"})
                return ret(response)
            except:
                response = JsonResponse({"error_code": 1, "msg": "something error"})
                return ret(response)
        elif(TYPE=='POST'):
            try:
                res = models.likeposts.objects.get(openid=openid,postid=ID)
                res.delete()
                response = JsonResponse({"error_code": 0, "msg": "success"})
                return ret(response)
            except:
                response = JsonResponse({"error_code": 1, "msg": "something error"})
                return ret(response) 
        elif(TYPE=='COMMENT'):
            try:
                res = models.likecomments.objects.get(openid=openid,commentid=ID)
                res.delete()
                response = JsonResponse({"error_code": 0, "msg": "success"})
                return ret(response)
            except:
                response = JsonResponse({"error_code": 1, "msg": "something error"})
                return ret(response)
        else:
            response = JsonResponse({"error_code": 1, "msg": "type error"})
            return ret(response)            
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
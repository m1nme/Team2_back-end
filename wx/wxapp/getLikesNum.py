from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def getLikesNum(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        TYPE = params['TYPE']
        ID = params['ID']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        if(TYPE=='CAT'):
            num = models.likecats.objects.filter(catid=ID).count()
            try:
            	models.likecats.objects.get(catid=ID,openid=openid)
            	liked = 1
            except:
            	liked = 0
        elif(TYPE=='POST'):
            num = models.likeposts.objects.filter(postid=ID).count()
            try:
            	models.likeposts.objects.get(postid=ID,openid=openid)
            	liked = 1
            except:
            	liked = 0
        elif(TYPE=='COMMENT'):
            num = models.likecomments.objects.filter(commentid=ID).count()
            try:
            	models.likecomments.objects.get(commentid=ID,openid=openid)
            	liked = 1
            except:
            	liked = 0
        else:
            response = JsonResponse({"error_code": 1, "msg": "type error"})
            return ret(response)
        response = JsonResponse({"error_code": 0, "msg": "success", "num": num, "liked": liked})
        return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
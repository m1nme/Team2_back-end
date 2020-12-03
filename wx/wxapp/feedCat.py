from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def feedCat(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        catid = params['catId']
        food = params['food']
        time = params['time']
        op = params['op']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        models.feed.objects.create(catid=catid,openid=openid,food=food,time=time,op=op)

        try:
            res = models.lastfeed.objects.get(catid=catid)
            res.time = time
            res.save()
        except:
            models.lastfeed.objects.create(catid=catid,time=time)

        response = JsonResponse({"error_code": 0, "msg": "success"})
        return ret(response)

    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
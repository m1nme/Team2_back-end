from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def modifyFeedLog(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        catid = params['catId']
        food = params['food']
        time = params['time']
        op = params['op']
        feedid = params['feedId']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        try:
            feed = models.feed.objects.get(openid=openid,id=feedid)
            feed.food = food
            feed.time = time
            feed.op = op
            feed.save()
            response = JsonResponse({"error_code": 0, "msg": "success"})
            return ret(response)
        except:
            response = JsonResponse({"error_code": 1, "msg": "feedId error"})
            return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
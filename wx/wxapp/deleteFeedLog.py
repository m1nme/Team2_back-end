from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def deleteFeedLog(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        feedid = params['feedId']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        try:
            feed = models.feed.objects.get(openid=openid,id=feedid)
            feed.delete()
            response = JsonResponse({"error_code": 0, "msg": "success"})
            return ret(response)
        except:
            response = JsonResponse({"error_code": 1, "msg": "feedId error"})
            return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
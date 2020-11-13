from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def getUserInfo(request):
    try:
        params = json.loads(request.body)
        openid = params['token']
        try:
        	models.token.objects.get(openid=openid)
        except:
	        response = JsonResponse({"error_code": 1, "msg": "please login first"})
	        return ret(response)        	

        user = models.user.objects.get(openid=openid)
        nickname = user.nickname
        url = user.url

        response = JsonResponse({"error_code": 0, "msg": "success", "data": {"nickName": nickname, "avatarUrl": url}})
        return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
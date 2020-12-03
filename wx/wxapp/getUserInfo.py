from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def getUserInfo(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        try:
            user = models.user.objects.get(openid=openid)
            nickname = user.nickname
            url = user.url
        except:
            nickname = "匿名用户"
            url = "https://iminx-1258939911.cos.ap-chengdu.myqcloud.com/fzucats/20201113230601.jpg"
            models.user.objects.create(openid=openid,nickname=nickname,url=url)
        response = JsonResponse({"error_code": 0, "msg": "success", "data": {"nickName": nickname, "avatarUrl": url}})
        return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
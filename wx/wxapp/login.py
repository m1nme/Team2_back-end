from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from wxapp import models
import time,hashlib
import json
from wx.ret import ret
from wx import secrets
import requests
import time

# 登录处理
def login(request):
    try:
        params = json.loads(request.body)
        code = params['code']
        url = "https://api.weixin.qq.com/sns/jscode2session"
        url = url + "?appid=" + secrets.app_id + "&secret=" + secrets.app_secret + "&js_code=" + code + "&grant_type=authorization_code"
        try:
            res = requests.get(url)
            openid = res.json()['openid']
            session_key = res.json()['session_key']
        except:
            response = JsonResponse({"error_code": 1, "msg": "invalid code"})
            return ret(response)

        token = openid + str(int(time.time()))
        md5 = hashlib.md5()
        md5.update(token.encode("utf-8"))
        token = md5.hexdigest()

        try:
            has_user = models.token.objects.get(openid=openid)
            has_user.sessionkey = session_key
            has_user.token = token
            has_user.save()
        except:
            models.token.objects.create(openid=openid,sessionkey=session_key,token=token)

        response = JsonResponse({"error_code": 0, "msg": "success", "data": {"token": token}})
        return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
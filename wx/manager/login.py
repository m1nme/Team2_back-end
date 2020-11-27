from django.http import JsonResponse
from wx.ret import ret
from manager import models
import json
from wx.secrets import salt_passwd,salt_jwt
import jwt
import datetime
import hashlib

def login(request):
    try:
        params = json.loads(request.body)
        username = params['username']
        password = str(params['password']) + salt_passwd
        password = hashlib.md5(password.encode())
        password = password.hexdigest()
        user = models.user.objects.get(username=username)
        passwd = user.password
        if(password==passwd):
            headers = {
                "typ": "jwt_",
                "alg": "HS256",
            }
            payload = {
                "user_type": "admin",
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=1440)
            }
            token = jwt.encode(payload=payload, key=salt_jwt, headers=headers).decode("utf-8")
            response = JsonResponse({"error_code":0, "token": token})
            return ret(response)
        else:
            response = JsonResponse({"error_code": 1, "msg": "username or password wrong"})
            return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
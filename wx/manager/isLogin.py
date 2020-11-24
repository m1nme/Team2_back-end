from django.http import JsonResponse
from wx.ret import ret
import json
from manager.verifyToken import verifyToken

def isLogin(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        result = verifyToken(token)
        if(result==True):
            response = JsonResponse({"error_code": 0, "msg": "success"})
            return ret(response)
        else:
            response = JsonResponse({"error_code": 1, "msg": result})
            return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
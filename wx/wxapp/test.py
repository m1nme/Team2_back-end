from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json


def getFeedLog(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        try:
            catid = params['catId']
        except:
            catid = 1
        op = params['op']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        data = []
        cat = {}
        if(op=='CAT'):
            results = models.feed.objects.filter(catid=catid)
            for i in results:
                cat = {"catId": i.catid,
                        "food": i.food,
                        "time": i.time,
                    }
        elif(op=='USER'):
            pass
        elif(op=='BRIEF'):
            pass
        response = JsonResponse({"error_code": 0, "msg": "success", "data": data})
        return ret(response)

    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
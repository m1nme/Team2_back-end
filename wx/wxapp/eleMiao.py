from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def eleMiao(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)

        res = models.lastfeed.objects.all().order_by('time')[:5]
        data = []
        for i in res:
            try:
                res2 = models.cats.objects.get(id=i.catid)
                info = {"catId": i.catid,"catUrl": res2.url,"catName": res2.name, "feedTime": i.time}
                data.append(info)
            except:
                pass

        response = JsonResponse({"error_code": 0, "msg": "success", "data": data})
        return ret(response)

    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
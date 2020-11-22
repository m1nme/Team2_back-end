from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def showCommentsLog(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        data = []
        comment = {}
        results = models.comments.objects.filter(openid=openid)
        for i in results:
            comment = {"commentId": i.id,
                    "content": i.content,
                    "time": i.modifytime,
                    "status": i.vet
                }
            data.append(comment)

        response = JsonResponse({"error_code": 0, "msg": "success", "data": data})
        return ret(response)

    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
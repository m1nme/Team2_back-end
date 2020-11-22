from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def showPostsLog(request):
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
        results = models.posts.objects.filter(openid=openid)
        for i in results:
            comment = {"postId": i.id,
                    "title": i.title,
                    "time": i.modifytime,
                    "status": i.vet
                }
            data.append(comment)

        response = JsonResponse({"error_code": 0, "msg": "success", "data": data})
        return ret(response)

    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
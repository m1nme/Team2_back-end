from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def latestPosts(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)

        res = models.posts.objects.filter(vet=1).order_by('modifytime')[:5]
        data = []
        for i in res:
            info = {"postId": i.id, "postTitle": i.title, "time": i.modifytime}
            data.append(info)

        response = JsonResponse({"error_code": 0, "msg": "success", "data": data})
        return ret(response)

    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
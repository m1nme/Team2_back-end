from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def showComments(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        postid = params['postId']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        data = []
        comment = {}
        results = models.comments.objects.filter(vet=1,postid=postid)
        for i in results:
            comment = {"commentId": i.id,
                    "userName": i.userurl,
                    "userUrl": i.username,
                    "content": i.content,
                    "time": i.modifytime
                }
            data.append(comment)

        response = JsonResponse({"error_code": 0, "msg": "success", "data": data})
        return ret(response)

    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
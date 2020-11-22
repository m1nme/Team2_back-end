from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def deleteComment(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        commentid = params['commentId']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        try:
            comment = models.comments.objects.get(openid=openid,id=commentid)
            comment.delete()
            response = JsonResponse({"error_code": 0, "msg": "success"})
            return ret(response)
        except:
            response = JsonResponse({"error_code": 1, "msg": "feedId error"})
            return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
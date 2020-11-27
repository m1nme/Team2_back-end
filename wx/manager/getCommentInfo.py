from django.http import JsonResponse
from wx.ret import ret
import json
from wxapp import models
from manager.verifyToken import verifyToken
from django.core.paginator import Paginator, EmptyPage

def getCommentInfo(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        commentid = params['commentId']

        result = verifyToken(token)
        if(result==True):
            try:
                comment = models.comments.objects.get(id=commentid)
                response = JsonResponse({"error_code": 0, "msg": "success", "data": {
                                                                                    "commentId": comment.id,
                                                                                    "commentContent": comment.content,
                                                                                    "username": comment.username,
                                                                                    "commentTime": comment.modifytime,
                                                                                    "commentVet": comment.vet
                                                                                    }})
                return ret(response)
            except:
                response = JsonResponse({"error_code": 1, "msg": "ID error"})
                return ret(response)
        else:
            response = JsonResponse({"error_code": 1, "msg": result})
            return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
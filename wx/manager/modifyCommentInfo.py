from django.http import JsonResponse
from wx.ret import ret
import json
from wxapp import models
from manager.verifyToken import verifyToken
from django.core.paginator import Paginator, EmptyPage

def modifyCommentInfo(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        commentid = params['commentId']
        commentcontent = params['commentContent']
        commentvet = int(params['commentVet'])

        result = verifyToken(token)
        if(result==True):
            try:
                comment = models.comments.objects.get(id=commentid)
                comment.content = commentcontent
                comment.vet = commentvet
                comment.save()
                response = JsonResponse({"error_code": 0, "msg": "success"})
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
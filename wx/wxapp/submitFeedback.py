from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def submitFeedback(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        op = params['op']
        content = params['content']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        if(op=='CAT'):
            feedbacktype = 1
            try:
                catid = params['catId']
                models.feedbacks.objects.create(openid=openid,
                                                catid=catid,
                                                content=content,
                                                feedbacktype=feedbacktype,
                                                answer='',
                                                vet=0)
                response = JsonResponse({"error_code": 0, "msg": "success"})
                return ret(response)
            except:
                response = JsonResponse({"error_code": 1, "msg": "params error"})
                return ret(response)
        elif(op=='POST'):
            feedbacktype = 2
            try:
                postid = params['postId']
                models.feedbacks.objects.create(openid=openid,
                                                postid=postid,
                                                content=content,
                                                feedbacktype=feedbacktype,
                                                answer='',
                                                vet=0)
                response = JsonResponse({"error_code": 0, "msg": "success"})
                return ret(response)
            except:
                response = JsonResponse({"error_code": 1, "msg": "params error"})
                return ret(response)
        elif(op=='COMMENT'):
            feedbacktype = 3
            try:
                commentid = params['commentId']
                models.feedbacks.objects.create(openid=openid,
                                                commentid=commentid,
                                                content=content,
                                                feedbacktype=feedbacktype,
                                                answer='',
                                                vet=0)
                response = JsonResponse({"error_code": 0, "msg": "success"})
                return ret(response)
            except:
                response = JsonResponse({"error_code": 1, "msg": "params error"})
                return ret(response)
        elif(op=='OTHER'):
            feedbacktype = 4
            try:
                models.feedbacks.objects.create(openid=openid,
                                                content=content,
                                                feedbacktype=feedbacktype,
                                                answer='',
                                                vet=0)
                response = JsonResponse({"error_code": 0, "msg": "success"})
                return ret(response)
            except:
                response = JsonResponse({"error_code": 1, "msg": "params error"})
                return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
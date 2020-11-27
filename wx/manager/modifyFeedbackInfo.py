from django.http import JsonResponse
from wx.ret import ret
import json
from wxapp import models
from manager.verifyToken import verifyToken
from django.core.paginator import Paginator, EmptyPage

def modifyFeedbackInfo(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        feedbackid = params['feedbackId']
        feedbackanswer = params['feedbackAnswer']
        feedbackvet = int(params['feedbackVet'])

        result = verifyToken(token)
        if(result==True):
            try:
                feedback = models.feedbacks.objects.get(id=feedbackid)
                feedback.answer = feedbackanswer
                feedback.vet = feedbackvet
                feedback.save()
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
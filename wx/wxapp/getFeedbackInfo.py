from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def getFeedbackInfo(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        feedbackid = params['feedbackId']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        try:
            feedback = models.feedbacks.objects.get(id=feedbackid,openid=openid)
            response = JsonResponse({
                                    "error_code": 0,
                                    "msg": "success",
                                    "data": {
                                        "type": feedback.feedbacktype,
                                        "content": feedback.content,
                                        "urlList": feedback.urllist,
                                        "answer": feedback.answer,
                                        "time": feedback.time,
                                        "vet": feedback.vet
                                        }
                                    })
            return ret(response)
        except:
            response = JsonResponse({"error_code": 1, "msg": "feedbackId error"})
            return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
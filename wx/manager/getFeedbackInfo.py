from django.http import JsonResponse
from wx.ret import ret
import json
from wxapp import models
from manager.verifyToken import verifyToken
from django.core.paginator import Paginator, EmptyPage

def getFeedbackInfo(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        feedbackid = params['feedbackId']

        result = verifyToken(token)
        if(result==True):
            try:
                feedback = models.feedbacks.objects.get(id=feedbackid)
                if(feedback.feedbacktype==1):
                	ID = feedback.catid
                elif(feedback.feedbacktype==2):
                	ID = feedback.postid
                elif(feedback.feedbacktype==3):
                	ID = feedback.commentid
                elif(feedback.feedbacktype==4):
                	ID = 0
                response = JsonResponse({"error_code": 0, "msg": "success", "data": {
                                                                                    "feedbackId": feedback.id,
                                                                                    "feedbackContent": feedback.content,
                                                                                    "urlList": feedback.urllist,
                                                                                    "feedbackAnswer": feedback.answer,
                                                                                    "feedbackType": feedback.feedbacktype,
                                                                                    "ID": ID,
                                                                                    "feedbackTime": feedback.time,
                                                                                    "feedbackVet": feedback.vet
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
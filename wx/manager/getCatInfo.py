from django.http import JsonResponse
from wx.ret import ret
import json
from wxapp import models
from manager.verifyToken import verifyToken
from django.core.paginator import Paginator, EmptyPage

def getCatInfo(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        catid = params['catId']

        result = verifyToken(token)
        if(result==True):
            try:
                cat = models.cats.objects.get(id=catid)
                response = JsonResponse({"error_code": 0, "msg": "success", "data": {
                                                                                    "catId": cat.id,
                                                                                    "catName": cat.name,
                                                                                    "catColor": cat.color,
                                                                                    "catSex": cat.sex,
                                                                                    "catCharacter": cat.character,
                                                                                    "catStatus": cat.status,
                                                                                    "catAddress": cat.address,
                                                                                    "catUrl": cat.url,
                                                                                    "urlList": cat.urllist,
                                                                                    "catVet": cat.vet,
                                                                                    "username": cat.username
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
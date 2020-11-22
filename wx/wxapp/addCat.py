from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def addCat(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        
        try:
            catname = params['catName']
            catcolor = params['catColor']
            catsex = params['catSex']
            catcharacter = params['catCharacter']
            catstatus = params['catStatus']
            cataddress = params['catAddress']
            caturl = params['catUrl']
            username = models.user.objects.get(openid=openid).nickname

            models.cats.objects.create(name=catname,
                                    color=catcolor,
                                    sex=catsex,
                                    character=catcharacter,
                                    status=catstatus,
                                    address=cataddress,
                                    url=caturl,
                                    openid=openid,
                                    username=username,
                                    vet=0)
            response = JsonResponse({"error_code": 0, "msg": "success"})
            return ret(response)
        except:
            response = JsonResponse({"error_code": 1, "msg": "params error"})
            return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
from django.http import JsonResponse
from wx.ret import ret
import json
from wxapp import models
from manager.verifyToken import verifyToken
from django.core.paginator import Paginator, EmptyPage

def modifyCatInfo(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        catid = params['catId']
        catname = params['catName']
        catcolor = params['catColor']
        catsex = params['catSex']
        catcharacter = params['catCharacter']
        catstatus = params['catStatus']
        cataddress = params['catAddress']
        caturl = params['catUrl']
        catvet = params['catVet']
        urllist = str(params['urlList'])

        result = verifyToken(token)
        if(result==True):
            try:
                cat = models.cats.objects.get(id=catid)
                cat.name = catname
                cat.color = catcolor
                cat.sex = catsex
                cat.character = catcharacter
                cat.status = catstatus
                cat.address = cataddress
                cat.url = caturl
                cat.urllist = urllist
                cat.vet = catvet
                cat.save()
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
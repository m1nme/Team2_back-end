from django.http import JsonResponse
from wx.ret import ret
import json
from wxapp import models
from manager.verifyToken import verifyToken
from django.core.paginator import Paginator, EmptyPage
import math

def showCats(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        TYPE = int(params['TYPE'])
        if(TYPE!=1 and TYPE!=0 and TYPE !=-1):
            response = JsonResponse({"error_code": 1, "msg": "params error"})
            return ret(response)
        pagenum = params['pageNum']      # 每页多少条
        pagesize = params['pageSize']    # 第几页
        result = verifyToken(token)
        if(result==True):
            data = []
            qs = models.cats.objects.filter(vet=TYPE)
            pgnt = Paginator(qs, pagesize)
            page = pgnt.page(pagenum)
            for i in page:
                cat = {
                    "catId": i.id,
                    "catName": i.name,
                    "catUrl": i.url
                }
                data.append(cat)

            response = JsonResponse({"error_code": 0, "msg": "success", "data": data, "nums": pgnt.count,"pages": max(1,math.ceil(pgnt.count // pagesize))})
            return ret(response)
        else:
            response = JsonResponse({"error_code": 1, "msg": result})
            return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json
from django.db.models import Q

def showCatsList(request):
    # try:
    params = json.loads(request.body)
    token = params['token']
    address = params['address']
    try:
        openid = models.token.objects.get(token=token).openid
    except:
        response = JsonResponse({"error_code": 1, "msg": "please login first"})
        return ret(response)
    data = []
    cat = {}
    if(address=='ELSE'):
        results = models.cats.objects.filter(Q(vet=1)&~Q(address='三区')&~Q(address='一区')&~Q(address='文楼')&~Q(address='科技园'))
        for i in results:
            cat = {"catId": i.id,
                    "catUrl": i.url,
                    "catName": i.name
                }
            data.append(cat)
    else:
        results = models.cats.objects.filter(vet=1,address=address)
        for i in results:
            cat = {"catId": i.id,
                    "catUrl": i.url,
                    "catName": i.name
                }
            data.append(cat)

    response = JsonResponse({"error_code": 0, "msg": "success", "data": data})
    return ret(response)

# except:
    response = JsonResponse({"error_code": 1, "msg": "params error"})
    return ret(response)
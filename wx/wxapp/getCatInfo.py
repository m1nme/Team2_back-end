from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def getCatInfo(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        catid = params['catId']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        try:
            cat = models.cats.objects.get(id=catid,vet=1)
            response = JsonResponse({
            						"error_code": 0,
            						"msg": "success",
            						"data": {
            							"catName": cat.name,
            							"catColor": cat.color,
            							"catSex": cat.sex,
            							"catCharacter": cat.character,
            							"catStatus": cat.status,
            							"catAddress": cat.address,
            							"catUrl": cat.url,
            							"userName": cat.username
										}
									})
            return ret(response)
        except:
            response = JsonResponse({"error_code": 1, "msg": "catId error"})
            return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def like(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        ID = params['ID']
        TYPE = params['TYPE']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        if(TYPE=='CAT'):
            try:
                models.cats.objects.get(id=ID)# 判断是否存在该猫猫
            except:
                response = JsonResponse({"error_code": 1, "msg": "ID error"})
                return ret(response)
            try:
                models.likecats.objects.get(catid=ID,openid=openid)# 判断是否已经关注过该猫猫
                response = JsonResponse({"error_code": 1, "msg": "you already liked it"})
                return ret(response)
            except:
                models.likecats.objects.create(openid=openid,catid=ID)
                response = JsonResponse({"error_code": 0, "msg": "success"})
                return ret(response)
        elif(TYPE=='POST'):
            try:
                models.posts.objects.get(id=ID)# 判断是否存在该帖子
            except:
                response = JsonResponse({"error_code": 1, "msg": "ID error"})
                return ret(response)
            try:
                models.likeposts.objects.get(postid=ID,openid=openid)# 判断是否已经关注过该帖子
                response = JsonResponse({"error_code": 1, "msg": "you already liked it"})
                return ret(response)
            except:
                models.likeposts.objects.create(openid=openid,postid=ID)
                response = JsonResponse({"error_code": 0, "msg": "success"})
                return ret(response)
        elif(TYPE=='COMMENT'):
            try:
                models.comments.objects.get(id=ID)# 判断是否存在该留言
            except:
                response = JsonResponse({"error_code": 1, "msg": "ID error"})
                return ret(response)
            try:
                models.likecomments.objects.get(commentid=ID,openid=openid)# 判断是否已经关注过该留言
                response = JsonResponse({"error_code": 1, "msg": "you already liked it"})
                return ret(response)
            except:
                models.likecomments.objects.create(openid=openid,commentid=ID)
                response = JsonResponse({"error_code": 0, "msg": "success"})
                return ret(response)
        else:
            response = JsonResponse({"error_code": 1, "msg": "type error"})
            return ret(response)            
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
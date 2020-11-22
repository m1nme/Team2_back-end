from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def publishPost(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        
        try:
            catid = params['catId']
            title = params['title']
            content = params['content']
            urllist = str(params['urlList'])
            if(len(title)>100 or len(content)>1000 or len(urllist)>1000):
                response = JsonResponse({"error_code": 0, "msg": "something too long"})
                return ret(response)                
            user = models.user.objects.get(openid=openid)
            username = user.nickname
            userurl =  user.url

            models.posts.objects.create(catid=catid,
                                        title=title,
                                        content=content,
                                        urllist=urllist,
                                        openid=openid,
                                        username=username,
                                        userurl=userurl,
                                        vet=0)
            response = JsonResponse({"error_code": 0, "msg": "success"})
            return ret(response)
        except:
            response = JsonResponse({"error_code": 1, "msg": "params error"})
            return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
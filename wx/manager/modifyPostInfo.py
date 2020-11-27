from django.http import JsonResponse
from wx.ret import ret
import json
from wxapp import models
from manager.verifyToken import verifyToken
from django.core.paginator import Paginator, EmptyPage

def modifyPostInfo(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        postid = params['postId']
        posttitle = params['postTitle']
        postcontent = params['postContent']
        urllist = str(params['urlList'])
        postvet = int(params['postVet'])

        result = verifyToken(token)
        if(result==True):
            try:
                post = models.posts.objects.get(id=postid)
                post.title = posttitle
                post.content = postcontent
                post.urllist = urllist
                post.vet = postvet
                post.save()
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
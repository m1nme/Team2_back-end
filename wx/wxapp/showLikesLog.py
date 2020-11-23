from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def showLikesLog(request):
    try:
        params = json.loads(request.body)
        token = params['token']
        TYPE = params['TYPE']
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        data = []
        res = {}
        if(TYPE=='CAT'):
            results = models.likecats.objects.filter(openid=openid)
            for i in results:
                cat = models.cats.objects.get(id=i.catid)
                res = {"catId": cat.id,
                        "catName": cat.name,
                        "catUrl": cat.url
                    }
                data.append(res)
        elif(TYPE=='POST'):
            results = models.likeposts.objects.filter(openid=openid)
            for i in results:
                post = models.posts.objects.get(id=i.postid)
                res = {"postId": post.id,
                        "postTitle": post.title
                    }
                data.append(res)
        elif(TYPE=='COMMENT'):
            results = models.likecomments.objects.filter(openid=openid)
            for i in results:
                comment = models.comments.objects.get(id=i.commentid)
                res = {"commentId": comment.id,
                        "commentContent": comment.content
                    }
                data.append(res)
        else:
            response = JsonResponse({"error_code": 1, "msg": "type error"})
            return ret(response)
        
        response = JsonResponse({"error_code": 0, "msg": "success", "data": data})
        return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)
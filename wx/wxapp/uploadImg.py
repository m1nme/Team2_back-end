from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
import requests
from wx import secrets
import datetime
import random
from django.http import JsonResponse
from wx.ret import ret
from wxapp import models
import json

def uploadImg(request):
    try:
        token = request.POST.get('token')
        try:
            openid = models.token.objects.get(token=token).openid
        except:
            response = JsonResponse({"error_code": 1, "msg": "please login first"})
            return ret(response)
        
        file_obj = request.FILES.get('image',None)
        stream = file_obj.chunks()
        res = upload(stream)
        
        if(res==False):
            response = JsonResponse({"error_code": 1, "msg": "upload failed"})
            return ret(response)
        else:
            response = JsonResponse({"error_code": 0, "msg": "success", "data": {"url": res}})
            return ret(response)
    except:
        response = JsonResponse({"error_code": 1, "msg": "params error"})
        return ret(response)

def upload(stream):
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    config = CosConfig(Region=secrets.region,
                        SecretId=secrets.secret_id,
                        SecretKey=secrets.secret_key,
                        Token=secrets.token,
                        Scheme=secrets.scheme)

    client = CosS3Client(config)
    # 网络流将以 Transfer-Encoding:chunked 的方式传输到 COS
    try:
        nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        filename = str(nowtime) + str(random.randint(0,100))
        key = '/fzucats/' + filename + '.jpg'
        url = 'https://iminx-1258939911.cos.ap-chengdu.myqcloud.com' + key
        response = client.put_object(
            Bucket='iminx-1258939911',
            Body=stream,
            Key=key
        )
        return url
    except:
        return False
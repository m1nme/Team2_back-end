from django.db import models

class user(models.Model):
    # 用户名
    username = models.CharField(max_length=50)
    # 密码
    password = models.CharField(max_length=50)

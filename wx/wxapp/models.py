from django.db import models

class token(models.Model):
    # 用户openid，唯一
    openid = models.CharField(max_length=50)
    # session_key
    sessionkey = models.CharField(max_length=50)
    # TOKEN
    token = models.CharField(max_length=50)
class user(models.Model):
    # 用户openid，唯一
    openid = models.CharField(max_length=50)
    # 昵称
    nickname = models.CharField(max_length=50)
    # 头像URL
    url = models.CharField(max_length=200)
class cats(models.Model):
    # 昵称
    name = models.CharField(max_length=50)
    # 花色
    color = models.CharField(max_length=50)
    # 性别
    sex = models.CharField(max_length=10)
    # 性格
    character = models.CharField(max_length=50)
    # 健康状态
    status = models.CharField(max_length=50)
    # 出没地址
    address = models.CharField(max_length=50)
    # 头像URL
    url = models.CharField(max_length=300)
    # 审核状态(-1:审核失败，1：审核通过，0：待审核)
    vet = models.IntegerField()
    # 提供信息的用户
    openid = models.CharField(max_length=50)
    # 提供信息的用户昵称
    username = models.CharField(max_length=50)
class feed(models.Model):
    # 猫猫ID
    catid = models.IntegerField()
    # 喂猫人ID
    openid = models.CharField(max_length=50)
    # 喂食的食物和量
    food = models.CharField(max_length=500)
    # 喂食时间
    time = models.CharField(max_length=100)
    # 投喂类型1为普通2为预约
    op = models.IntegerField(default=1)
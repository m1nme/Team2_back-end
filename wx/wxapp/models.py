from django.db import models

# Create your models here.
class token(models.Model):
    openid = models.CharField(max_length=50)

    sessionkey = models.CharField(max_length=50)

    token = models.CharField(max_length=50)




class user(models.Model):
    openid = models.CharField(max_length=50)

    nickname = models.CharField(max_length=50)

    url = models.CharField(max_length=200)
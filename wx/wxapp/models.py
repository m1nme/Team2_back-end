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
class posts(models.Model):
    # 发帖人ID
    openid = models.CharField(max_length=50)
    # 发帖人昵称
    username = models.CharField(max_length=50)
    # 发帖人头像URL
    userurl = models.CharField(max_length=200)
    # 猫猫ID
    catid = models.IntegerField()
    # 帖子标题
    title = models.CharField(max_length=100)
    # 帖子内容
    content = models.CharField(max_length=1000)
    # 帖子图片列表
    urllist = models.CharField(max_length=1000)
    # 发帖时间
    modifytime = models.DateTimeField(auto_now_add=True)
    # 状态（0待审核，1审核通过，-1审核未通过）
    vet = models.IntegerField()
class comments(models.Model):
    # 留言者ID
    openid = models.CharField(max_length=50)
    # 留言者昵称
    username = models.CharField(max_length=50)
    # 留言者头像URL
    userurl = models.CharField(max_length=200)
    # 留言所属的帖子ID
    postid = models.IntegerField()
    # 留言内容
    content = models.CharField(max_length=300)
    # 状态（0待审核，1通过审核，-1未通过审核）
    vet = models.IntegerField()
    # 留言时间
    modifytime = models.DateTimeField(auto_now_add=True)
class feedbacks(models.Model):
    # 反馈者ID
    openid = models.CharField(max_length=50)
    # 反馈关于的猫猫ID
    catid = models.IntegerField(null=True)
    # 反馈关于的帖子ID
    postid = models.IntegerField(null=True)
    # 反馈关于的留言ID
    commentid = models.IntegerField(null=True)
    # 反馈类型(1为关于猫猫的反馈，2为关于帖子的反馈，3为关于留言的反馈，4为其它反馈)
    feedbacktype = models.IntegerField()
    # 反馈内容
    content = models.CharField(max_length=300)
    # 反馈回复
    answer = models.CharField(max_length=300,null=True)
    # 反馈状态(0为待回复，1为已回复)
    vet = models.IntegerField()
    # 反馈提交时间
    time = models.DateTimeField(auto_now_add=True)
class likecats(models.Model):
    # 关注者ID
    openid = models.CharField(max_length=50)
    # 关注的猫猫ID
    catid = models.IntegerField()
class likeposts(models.Model):
    # 关注者ID
    openid = models.CharField(max_length=50)
    # 帖子ID
    postid = models.IntegerField()
class likecomments(models.Model):
    # 关注者ID
    openid = models.CharField(max_length=50)
    # 留言ID
    commentid = models.IntegerField()
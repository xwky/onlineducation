from django.db import models
from course.models import *

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=11,verbose_name='用户名/手机号',unique=True)
    password = models.CharField(max_length=255,verbose_name='密码')
    birthday = models.DateField(verbose_name='生日',null=True)
    gender = models.CharField(max_length=32,verbose_name='性别',choices=(('male','男'),('female','女')),default='')
    address = models.CharField(max_length=128,verbose_name='地址',null=True)
    # upload_to值为头像存在本地的地址
    image = models.ImageField(upload_to='image/%Y/%m',default='image/default.jpg',max_length=128)
    # 多对多关联
    courses = models.ManyToManyField(Course)
    class Meta:
        db_table = 'userprofile'
        verbose_name = '用户基本信息表'
        verbose_name_plural = verbose_name
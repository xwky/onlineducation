from django.db import models
from datetime import datetime
from user.models import *
from course.models import *
from organization.models import *

# Create your models here.
class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    course_name = models.CharField(max_length=50, verbose_name='课程名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        db_table = 'userask'
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE, verbose_name='用户')
    course = models.ForeignKey(Course, verbose_name='课程',on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        db_table = 'coursecomments'
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name

class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户',on_delete=models.CASCADE)
    # ID 是课程的 ID 或者是 讲师、课程机构的 ID
    fav_id = models.IntegerField(default=0, verbose_name='收藏数据 Id')
    fav_type = models.IntegerField(choices=( (1, '课程'), (2, '课程机构'), (3, '讲师') ), default=1, verbose_name='收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        db_table = 'userfavorite'
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

class UserMessage(models.Model):
    # 如果 为 0 代表全局消息，否则就是用户的 ID
    user = models.IntegerField(default=0, verbose_name='接收用户')
    message = models.CharField(max_length=500, verbose_name='消息内容')
    has_read = models.BooleanField(default=False, verbose_name='是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


# CourseComments 和 UserCourse 字段差不多，可以使用 UserCourse 继承 CourseComments
class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户',on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='课程',on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户学习过的课程'
        verbose_name_plural = verbose_name


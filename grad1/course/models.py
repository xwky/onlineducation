from django.db import models
from datetime import datetime
from organization.models import *

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=128,verbose_name='课程名称')
    desc = models.CharField(max_length=256,verbose_name='课程描述')
    detail = models.TextField(max_length=255,verbose_name='课程详情')
    degree = models.CharField(max_length=5,verbose_name='课程等级')
    learn_time = models.IntegerField(default=0,verbose_name='课程时长')
    students = models.IntegerField(default=0,verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0,verbose_name='收藏人数')
    click_nums = models.IntegerField(default=0,verbose_name='点击人数')
    image = models.CharField(max_length=255,verbose_name='封面图')
    image_2 = models.CharField(max_length=255,verbose_name='小图片',default='')
    course_org = models.ForeignKey(CourseOrg,verbose_name='课程机构',on_delete=models.CASCADE,null=True, blank=True)
    teacher = models.ForeignKey(Teacher,verbose_name='讲师',on_delete=models.CASCADE,null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        db_table = 'course'
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name='章节名')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Met:
        db_table = 'lesson'
        verbose_name = '章节'
        verbose_name_plural = verbose_name

class Video(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE,default='')
    lesson = models.ForeignKey(Lesson,verbose_name='章节',on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name='视频名')
    url = models.URLField(max_length=500,verbose_name='访问地址',default='www.baidu.com')
    learn_times = models.IntegerField(default=0,verbose_name='视频时长')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        db_table = 'video'
        verbose_name = '视频'
        verbose_name_plural = verbose_name

class Freeback(models.Model):
    title = models.CharField(max_length=255,verbose_name='反馈标题')
    detail = models.CharField(max_length=1000,verbose_name='反馈内容')
    class Meta:
        db_table = 'freeback'
        verbose_name = '反馈'
        verbose_name_plural = verbose_name
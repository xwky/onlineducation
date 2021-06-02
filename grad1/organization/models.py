from django.db import models
from datetime import datetime

# Create your models here.
class CityDict(models.Model):
    name = models.CharField(max_length=20,verbose_name='城市')
    desc = models.TextField(verbose_name='城市描述')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        db_table = 'citydict'
        verbose_name = '城市'
        verbose_name_plural = verbose_name

class CourseOrg(models.Model):
    name = models.CharField(max_length=50,verbose_name='机构名称')
    category = models.CharField(max_length=20,default='培训机构',verbose_name='机构类别')
    desc = models.TextField(verbose_name='机构描述')
    tag = models.CharField(default='全国知名',max_length=10,verbose_name='机构标签')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    city = models.ForeignKey(CityDict,on_delete=models.CASCADE, verbose_name='所在城市')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    students = models.IntegerField(default=0, verbose_name='学习人数')

    class Meta:
        db_table = 'courseorg'
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name

class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,verbose_name='所属机构',on_delete=models.CASCADE)
    name = models.CharField(max_length=50,verbose_name='教师名字')
    work_year = models.IntegerField(default=0,verbose_name='工作年限')
    work_company = models.CharField(max_length=50,verbose_name='就职公司')
    work_position = models.CharField(max_length=50,verbose_name='公司职位')
    points = models.CharField(max_length=50,verbose_name='教学特点')
    click_nums = models.IntegerField(default=0,verbose_name='点击数')
    fav_nums = models.IntegerField(default=0,verbose_name='收藏数')
    age = models.IntegerField(default=30,verbose_name='年龄')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        db_table = 'teacher'
        verbose_name = '教师'
        verbose_name_plural = verbose_name
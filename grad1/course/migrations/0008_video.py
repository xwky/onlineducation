# Generated by Django 2.2.1 on 2020-03-08 08:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='视频名')),
                ('url', models.URLField(default='www.baidu.com', verbose_name='访问地址')),
                ('learn_times', models.IntegerField(default=0, verbose_name='视频时长')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Lesson', verbose_name='章节')),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': '视频',
                'db_table': 'video',
            },
        ),
    ]

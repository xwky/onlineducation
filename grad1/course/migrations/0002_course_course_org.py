# Generated by Django 2.2.1 on 2020-03-08 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_org',
            field=models.CharField(default='爱学习', max_length=255, verbose_name='课程机构'),
        ),
    ]

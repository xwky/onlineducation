# Generated by Django 2.2.1 on 2020-03-27 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_video_course'),
        ('user', '0003_auto_20200305_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='course',
            field=models.ManyToManyField(to='course.Course'),
        ),
    ]

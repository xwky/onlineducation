# Generated by Django 2.2.1 on 2020-03-26 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_video_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='course',
        ),
    ]

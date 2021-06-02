from rest_framework import serializers
from course.models import *
from operation.models import *
class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

class MyCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class AddCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course,UserProfile
        fields = '__all__'

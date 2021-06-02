from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from course.models import *
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from course.serializers import *
from haystack.views import SearchView
from django.http import JsonResponse
import json


from django.forms.models import  model_to_dict


# Create your views here.

# 免费课程
@api_view(['GET'])
def freecourse(request):
    freecourselist = Course.objects.filter(desc='free').all()
    res = {
        "freecourse":CourseListSerializer(freecourselist,many=True).data
    }
    return Response(res)


# 全部课程
@api_view(['GET'])
def allcourse(request):
    allcourselist = Course.objects.all()
    res = {
        "allcourse":CourseListSerializer(allcourselist,many=True).data
    }
    return Response(res)

# 实战课程
@api_view(['GET'])
def practicalcourse(request):
    practicalcourselist = Course.objects.exclude(desc='free').all()
    res = {
        "practicalcourse":CourseListSerializer(practicalcourselist,many=True).data
    }
    return Response(res)

# 首页新课
@api_view(['GET'])
def newcourse(request):
    newcourselist = Course.objects.filter(desc='new').all()
    res = {
        "newcourse":CourseListSerializer(newcourselist,many=True).data
    }
    return Response(res)

# 热门课程
@api_view(['GET'])
def hotcourse(request):
    hotcourselist = Course.objects.filter(desc='hot').all()
    res = {
        "hotcourse":CourseListSerializer(hotcourselist,many=True).data
    }
    return Response(res)

# 课程筛选
@api_view(['GET'])
def selectcourse(request):
    if request.method == 'GET':
        tag = request.GET.get('tag')
    print(tag)
    selectcourselist = Course.objects.filter(desc=tag).all()
    res = {
        "selectcourse":CourseListSerializer(selectcourselist,many=True).data
    }
    return Response(res)


# 点击次数

@api_view(['GET'])
def clicknums(request):
    if request.method == 'GET':
        cid = request.GET.get('cid')
        count = request.GET.get('count')
        print(count)
        if count:
            course = Course.objects.get(id=cid)
            course.fav_nums += 1
            course.save(update_fields=['fav_nums'])
            print(course.fav_nums)



# 课程详情页
@api_view(['GET'])
def coursedetail(request):
    # cid = request.data['cid']
    # cid = request.GET.get('cid')
    if request.method == 'GET':
        cid = request.GET.get('cid')




    # 课程
    courseid = Course.objects.filter(id=cid)

    # 课程章节名称
    course_lesson = Lesson.objects.filter(course_id=cid).all()

    # 视频名称
    lesson_video = Video.objects.filter(course_id=cid)
    # lesson_video = Video.objects.filter(lesson_id=course_lesson.id).all()

    res = {
        "course":CourseListSerializer(courseid,many=True).data,
        "course_lesson":LessonSerializer(course_lesson,many=True).data,
        "lesson_video":VideoSerializer(lesson_video,many=True).data
        }
    return Response(res)




# 搜索课程
@api_view(['GET'])
def searchcourse(request):
    if request.method == 'GET':
        searchmessage = request.GET.get('searchData')
    print(searchmessage)
    course = Course.objects.filter(name__icontains=searchmessage)
    res = {
        'searchcourse':CourseListSerializer(course,many=True).data
    }
    return Response(res)

# 添加收藏课程
@api_view(['GET', 'POST'])
def addcourse(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        print('req',req)
        uid = int(req['uid'])
        cid = int(req['cid'])
        print('uid',uid,cid)
        if uid and cid:
            user = UserProfile.objects.filter(id=uid).first()
            cou = Course.objects.filter(id=cid).first()
            course = Course.objects.get(id=cid)
            print('学生',course.students)
            user.courses.add(cou)
            user.save()
            res = {
                'code':200,
                'msg':'收藏成功'
            }
            return Response(res)

# 删除收藏课程
@api_view(['GET', 'POST'])
def delecourse(request):
    if request.method == 'POST':
        reu = json.loads(request.body)
        # print('reu',reu)
        uid = int(reu['uid'])
        cid = int(reu['cid'])
        print('uid2', uid, cid)
        if uid and cid:
            user = UserProfile.objects.filter(id=uid).first()
            cou = Course.objects.filter(id=cid).first()
            # print(cou.id)
            user.courses.remove(cou)
            user.save()
            res = {
                'code':200,
                'msg':'删除成功'
            }
            return Response(res)
# 查看我的课程
@api_view(['GET'])
def mycourse(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        print('2',uid)
        stu = UserProfile.objects.get(id=uid)
        print(stu.id)
        mycourse = stu.courses.all()
        print('mycourse',mycourse)
        for i in mycourse:
            print(i.name)

    res = {
        'mycourse':MyCourseSerializer(mycourse,many=True).data,
        # 'courses':CourseListSerializer(courses,many=True).data
    }
    return Response(res)

# 课程反馈

@api_view(['POST'])
def freeback(request):
    if request.method == 'POST':
        info = json.loads(request.body)
        if info['title'] != '' and info['info'] !='':
            title = info['title']
            detail = info['info']
            Freeback.objects.create(title=title,detail=detail)
            res = {
                'code':200,
                'msg':'反馈成功'
            }
            return Response(res)
        else:
            res = {
                'code': 400,
                'msg': '反馈失败'
            }
            return Response(res)







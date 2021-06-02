from .models import Course
import xadmin

class CourseAdmin(object):
    # 设置后台显示字段
    list_display = ('name','desc','detail','degree','learn_time','students','fav_nums','click_nums','image','add_time','image_2','course_org','teacher')
    # 后台搜索字段
    search_fields = ['name','desc','detail','degree']
#     后台过滤字段
    list_filter = ['name','desc','detail','degree']

xadmin.site.register(Course,CourseAdmin)
from course import *
from rest_framework.routers import SimpleRouter
from course.views import *
from django.urls import path,include
from course import views
from django.conf.urls import url

route = SimpleRouter()
# route.register("create_response",MySearchView)
# route.register('')

urlpatterns = [
    path('freecourse/',freecourse),
    path(r'coursedetail/',views.coursedetail),
    path('allcourse/',views.allcourse),
    path('practicalcourse/',views.practicalcourse),
    path('selectcourse/',views.selectcourse),
    path('searchcourse/',views.searchcourse),
    path('newcourse/',views.newcourse),
    path('hotcourse/',views.hotcourse),
    path('mycourse/',views.mycourse),
    path('addcourse/',views.addcourse),
    path('delecourse/',views.delecourse),
    path('freeback/',views.freeback),
    path('clicknums/',views.clicknums),
    # url(r'^search/', include('haystack.urls')),#添加该代码
    # path('search/',MySearchView())
]
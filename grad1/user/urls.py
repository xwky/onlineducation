from rest_framework.routers import SimpleRouter
from user.views import *
from django.urls import path,include
from user import views

route = SimpleRouter()
route.register("login",LoginView)
route.register("register",RegisterView)
# route.register('userinfo',UserInfoView)

urlpatterns = [

    path('userinfo/',userinfo)

]
urlpatterns += route.urls
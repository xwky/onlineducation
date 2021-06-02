from django.shortcuts import render
from rest_framework import viewsets
# from user.models import *
from user.serializers import *
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# 注册
class LoginView(viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = LoginSerializer
    @action(methods=["POST"],detail=False)
    def login(self,request):
        # 序列化
        serializer = self.get_serializer(data=request.data)
        #验证
        result = serializer.is_valid()
        print('1', serializer.data)
        print('2',result)
        #保存到数据库
        data = serializer.login_data(serializer.data)
        print('3',data)
        return Response(data)

#登录

class RegisterView(viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = RegisterSerializer
    @action(methods=['POST'],detail=False)
    def register(self,request):
        print(request.data)
        serializer = RegisterSerializer(data=request.data)
        result = serializer.is_valid()
        print(result)
        print(serializer.data)
        # if result:
        res = serializer.register_data(serializer.data,request)
        print(res)
        return Response(res)




@api_view(['GET'])
def userinfo(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
    print('userinfo',uid)

    userinfomation = UserProfile.objects.filter(id=uid)

    res = {
        'userinfo':InfoSerializer(userinfomation,many=True).data
    }
    return Response(res)

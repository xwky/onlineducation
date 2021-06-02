from user.models import *
from rest_framework import serializers
from utils.error import *
from django.contrib.auth.hashers import make_password,check_password


#注册
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required= True,max_length=11,min_length=11,error_messages={
        "required":"注册账户必填",
        "max_length":"请输入11位手机号",
        "min_length":"请输入11位手机号"
    })
    password = serializers.CharField(required=True,max_length=32,min_length=4,error_messages={
        "required":"密码必填",
        "max_length":"密码不超过32位",
        "min_length":"密码不能少于6位"
    })
    password2 = serializers.CharField(required=True,max_length=32,min_length=4,error_messages={
        "required": "密码必填",
        "max_length": "密码不超过32位",
        "min_length": "密码不能少于6位"
    })
    birthday = serializers.DateField(required=False)
    address = serializers.CharField(required=False)

    class Meta:
        model = UserProfile
        fields = ("__all__")

    def validate(self, attrs):
        username = attrs['username']
        return attrs


    def login_data(self,validate_data):
        if UserProfile.objects.filter(username=validate_data['username']).exists():
            res = {
                "code": 123, "msg": "该用户已经存在"
            }
            return res
        print(validate_data)
        password = make_password(validate_data["password"])
        user = UserProfile.objects.create(username = validate_data["username"],
                                          password = password)

        res = {
            "code":200,
            "msg":"注册成功",
            "user_id":user.id
        }
        return res

#登录
class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, max_length=11, min_length=11, error_messages={
        "required": "注册账户必填",
        "max_length": "请输入11位手机号",
        "min_length": "请输入11位手机号"
    })
    password = serializers.CharField(required=True, max_length=32, min_length=4, error_messages={
        "required": "密码必填",
        "max_length": "密码不超过32位",
        "min_length": "密码不能少于4位"
    })
    class Meta:
        model = UserProfile
        fields = "__all__"

    def validate(self, attrs):
        return attrs

    def register_data(self,validate_data,request):
        if not UserProfile.objects.filter(username=validate_data["username"]).exists():
            res = {
                "code": 123,
                "msg": "用户不存在",
            }
            return res
        user = UserProfile.objects.filter(username=validate_data['username']).first()
        if not check_password(validate_data.get('password'),user.password):
            res = {"code": 456, "msg": "密码错误"}
            return res
        else:
            request.session["user_id"] = user.id
            res = {
                "code": 200,
                "msg": "登录成功",
                "user_id": user.id
            }
            return res

# 个人页面
class UserInfoSerializer(serializers.Serializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

    uid = serializers.CharField(required=False)
    def validate(self, attrs):
        # uid = attrs['uid']
        # print('1',uid)
        return attrs

    def user_data(self,validate_data,request):
        uid = request.session['user_id']
        print('2',uid)
        if uid:
            user = UserProfile.objects.filter(id=uid).all()
            res = {
                'username':user.username,
                'birthday':user.birthday,
                'gender':user.gender,
                'address':user.address,
                'image':user.image
            }
            return res
        else:
            res = {
                "code": 147,
                "msg": "用户没有登录"
            }
            return res

#个人页面
class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
from .models import *
import xadmin

class UserProfileAdmin(object):
    list_display = ('username','password','birthday','gender','address','image','courses')

xadmin.site.register(UserProfile,UserProfileAdmin)
from django.shortcuts import render

from django.views.generic.base import View
from django.contrib.auth import authenticate


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        # 设置默认值为空
        user_name = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # 用于通过用户和密码查询用户是否存在
        user = authenticate(username=user_name, password=password)

        # from apps.users.models import UserProfile
        # user = UserProfile.objects.get(username=user_name, password=password)

        '''
        这种方式校验有两个问题
        1.通过用户名查询用户，但可能密码不对
        2.再通过密码校验，但是数据库存储的是加密后的值，得先自己加密再比较，很麻烦，
        也不利于后期其功能的扩展和维护
        '''

        if (user is not None):
            pass

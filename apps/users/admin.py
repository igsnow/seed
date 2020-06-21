from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    pass


# 将模型注册到admin,直接使用自定义的UserProfileAdmin会造成创建用户时密码没有加密的情况
admin.site.register(UserProfile, UserAdmin)

"""seed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
import xadmin

# 导入自定义的LoginView
from apps.users.views import LoginView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    # 代替之前自己定义def函数的render方法
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # 给跳转路径起一个名字，给指定的跳转模板文件使用，到时只要更改path的第一个参数即可
    # 使用自己定义的View进行登录校验逻辑
    path('login/', LoginView.as_view(), name='login')
]

# 实现视图有两种  CBV(class base view) 、 FBV(function base view)
# 主要用前者

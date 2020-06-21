from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'apps.users'
    # 修改admin后台站点管理下面模块的标题
    verbose_name = '用户'

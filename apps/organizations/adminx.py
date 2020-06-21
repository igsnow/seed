import xadmin

from apps.organizations.models import Teacher, CourseOrg, City


# 可以不继承任何东西，于是这里可以继承object
class TeacherAdmin(object):
    pass


class CourseOrgAdmin(object):
    pass


class CityAdmin(object):
    # 配置列表展示列
    list_display = ['id', 'name', 'desc']
    # 配置列表搜索条件
    search_fields = ['name', 'desc']
    # 配置过滤器
    list_filter = ['name', 'desc', 'add_time']
    # 配置列表字段是否能编辑
    list_editable = ['name', 'desc']


xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(City, CityAdmin)

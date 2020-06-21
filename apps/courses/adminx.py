import xadmin

from apps.courses.models import Course, Lesson, Video, CourseResource


# xadmni的全局配置
class GlobalSettings(object):
    # 左上角标题
    site_title = '剑网3后台管理系统'
    # 底部文字
    site_footer = '稻香村'


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


# 可以不继承任何东西，于是这里可以继承object
class CourseAdmin(object):
    # 配置列表展示列
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    # 配置列表搜索条件
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    # 配置过滤器
    list_filter = ['name', 'teacher__name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    # 配置列表字段是否能编辑
    list_editable = ['degree', 'desc']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    # 由于course是个外键，直接过滤肯定不行，外键加上双下划线拼接具体字段可进行过滤
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'file', 'add_time']
    search_fields = ['course', 'name', 'file']
    list_filter = ['course', 'name', 'file', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)

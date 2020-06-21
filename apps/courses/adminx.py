import xadmin

from apps.courses.models import Course


# 可以不继承任何东西，于是这里可以继承object
class CourseAdmin(object):
    pass


xadmin.site.register(Course, CourseAdmin)

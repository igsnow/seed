from django.db import models
from apps.users.models import BaseModel

# 设计表结构注意事项
# 实体和实体之间存在关系，一对多等
"""
课程 章节 视频 资源
"""


# 找到课程实体的具体字段

# 字段类型，是否必填


class Course(BaseModel):
    name = models.CharField(max_length=50, verbose_name="课程名")
    desc = models.CharField(max_length=300, verbose_name="课程描述")
    learn_times = models.IntegerField(default=0, verbose_name='学习时长(分钟数)')
    degree = models.CharField(verbose_name='难度', choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')), max_length=2)
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    category = models.CharField(default='后端开发', max_length=20, verbose_name='课程类别')
    tag = models.CharField(default='', verbose_name='课程标签', max_length=10)
    youneed_know = models.CharField(default='', max_length=300, verbose_name='课程须知')
    teacher_tell = models.CharField(default='', max_length=300, verbose_name='老师告诉你')
    detail = models.TextField(verbose_name='课程详情')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图', max_length=100)

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name


class Lesson(BaseModel):
    # on_delete 表示对应的外键数据被删除后，当前的数据应该怎么办
    # 如果on_delete设置为model.SET_NULL，则需要配置 null = True , blank = True，不然django报错
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='章节名')
    learn_times = models.IntegerField(default=0, verbose_name='学习时长(分钟数)')

    class Meta:
        verbose_name = '课程章节'
        verbose_name_plural = verbose_name



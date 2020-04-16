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
    
    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name

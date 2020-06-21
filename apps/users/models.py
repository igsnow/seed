from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

# 第一个值是存在数据库中的值
GENDER_CHOICE = (
    ('male', '男'),
    ('female', '女')
)


# 将这个类放到最底层，避免被其他模块import
class BaseModel(models.Model):
    # 注意不能直接调用.now()方法，会在程序编译时就生成时间了，不是想要的结果
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        # 防止migrate时生成一张表
        abstract = True


class UserProfile(AbstractUser):
    # null=True,blank=True 非必填字段的一种表示方法，default表示必填， 不过开始可以设置一个空字符串
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='')
    # 生日设置当前时间默认值明显不合适(default)，于是采用第一种方式
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(max_length=6, verbose_name='性别', choices=GENDER_CHOICE)
    address = models.CharField(max_length=100, verbose_name='地址', default='')
    mobile = models.CharField(max_length=11, verbose_name='手机号码', unique=True)
    # 配置到media文件夹下面
    image = models.ImageField(verbose_name='用户头像', upload_to='head_image/%Y/%m', default='default.jpg')

    class Meta:
        # 记录表的信息，比如表名
        verbose_name = '用户信息'
        # 后台系统显示用到，如果不设置，会将表名显示成"用户信息s"
        verbose_name_plural = verbose_name
        # db_table = 'my_user'  手动设置表名

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username

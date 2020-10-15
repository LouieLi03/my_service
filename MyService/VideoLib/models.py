from datetime import datetime, date

from django.db import models


# Create your models here.

class BaseModel(models.Model):

    # 将属性和属性值转换成dict 列表生成式
    def toDict(self):
        # type(self._meta.fields).__name__
        data = {}
        fields = []
        for field in self._meta.fields:
            fields.append(field)

        for attr in fields:
            val = getattr(self, attr.name)
            key = attr.name
            print(type(val))

            if type(val) == datetime:
                print(val.strftime('%Y-%m-%d %H:%M:%S'))
                val = val.strftime('%Y-%m-%d %H:%M:%S')

            if type(val) == date:
                print(val.strftime('%Y-%m-%d'))
                val = val.strftime('%Y-%m-%d')

            data[key] = val
        return data

    class Meta:
        # 一个抽象模型。抽象模型本身不实际生成数据库表，而是作为其它模型的父类，被继承使用
        abstract = True


class User(BaseModel):
    user_no = models.AutoField(primary_key=True)
    token = models.CharField(max_length=32)
    username = models.CharField(max_length=32, unique=True, null=False)
    mobile_no = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)
    # 0:未知 1:男 2:女
    sex = models.IntegerField(default=0)
    password = models.CharField(max_length=255, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    # 将属性和属性值转换成dict 列表生成式
    def toDict(self):
        data = super().toDict()
        data.pop("password")
        data.pop("is_delete")
        return data

    class Meta:
        db_table = 'video_lib_user'

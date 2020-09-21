from django.db import models


# Create your models here.


class User(models.Model):
    user_no = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, unique=True, null=False)
    mobile_no = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d/')
    # 0:未知 1:男 2:女
    sex = models.IntegerField(default=0)
    password = models.CharField(max_length=255, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'video_lib_user'

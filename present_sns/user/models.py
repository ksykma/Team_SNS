from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class UserModel(AbstractUser): # 적용하기 위해서 admin.py에서 적용 시켜주어야 함
    class Meta:
        db_table = "user_table"
        # 테이블 이름을 나타냄
    username = models.CharField(max_length=20,null=False,unique=True)
    password = models.CharField(max_length=256,null=False)
    bio = models.CharField(max_length=256, default='')
    # user model을 가져왔고 bio 만 추가해서 사용
    nickname = models.CharField(max_length=8, default='', blank=False, unique=True)
    user_img = models.ImageField(upload_to='user', null=True, blank=True, default=None)
    phone = models.CharField(max_length=256,null=True,unique=True)


# class Follow(models.Model):
#     follow = models.ManyToManyField('User', on_delete=models.CASCADE, related_name='to_user')
#     following = models.ManyToManyField('User', on_delete=models.CASCADE, related_name='from_user')

#     class Meta:
#         db_table = 'follow'

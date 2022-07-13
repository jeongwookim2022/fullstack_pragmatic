from django.contrib.auth.models import User
from django.db import models

# Create your models here.

######################################################################

# Profile객체와 user객체를 1 to 1으로 연결해줌
# User는 admin에서 정한 각 user를 나타내는 객체의 변수명
# 즉, 아래의 'user'를 현재 사용중인'User'와 연결.

# on_delete=models.CASCADE
# --> 연결 되어있는 User객체가 delete될 때,
# 이 Profile 클래스의 객체도 delete되도록 함.

# related_name='profile'
# --> EX) request.user.profile.nickname 등으로 속성을 쉽게 갖고
# 올 수 있도록 함.

#image = models.ImageField(upload_to='')
# --> upload_to='' 이미지를 받아서 서버 어디에 저장
# 즉, /media/profile/ 이 경로에 이미지가 저장될 것임.
# null=True --> 꼭 프로필 안 올려도 됨

# nickname = models.CharField(max_length=20, unique=True, null=Ture)
# --> (1) unique는 오직 유일한 닉네임이어야 한다
# (2) null=True로 해놓게 나중에 Ture라면 닉네임을 설정하라고 구현할 것임.
# (3) Form을 만들어서 설정한다.
# // Accountapp에서는 django에서 기본적으로 제공해서 안 만들고 사용했음.
# // 그렇지만 새로운 form을 일일이 다 코딩하기엔 너무 많음.
# // --> Model Form을 사용하여 작성한 MODEL(CLASS)를 FORM으로 바꿀 수 있음.

class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)

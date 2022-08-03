from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# on_delete=models.SET_NULL
# - 회원 탈퇴하더라도 사라지지 않고, "주인 없음" 등으로 남김
# related_name='article'인 것은, User객체가 Article에 접근 할 때
# 쓰는 이름으로 article이 더 직관적이다.

#title
# - null=True 꼭 제목이 있을 필요는 없다는 것.

# created_at
# - 언제 만들어졌는지 확인 가능
# - auto_created=True -> 자동으로 생성 시간이 저장됨
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    # 어느 project에 들어갈지// Projectapp과의 연결고리
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_created=True, null=True)

    when = models.DateTimeField(auto_now_add=True)

    # Like System
    like = models.IntegerField(default=0)
    # DisLike System
    dislike = models.IntegerField(default=0)




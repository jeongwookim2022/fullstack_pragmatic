from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# 어떤 user와 어떤 project 그 쌍이 가지는 구독 정보가
# 1개가 되도록 해야 함. --> 즉, 구독 1번만 가능해야 함.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='subscription')

    # 구독 1번만 가능하도록 하기 위해서.
    # --> user와 project가 가지는 subscription이 오직 1쌍이 되도록 함.
    class Meta:
        unique_together = ('user', 'project')


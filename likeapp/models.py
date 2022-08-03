from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class LikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='like_record')
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='like_record')

    # 1 user가 1 article에 1개의 like만 할 수 있도록
    # --> user와 article의 like에 대한 set이 1개만 존재하도록 설정.
    class Meta:
        unique_together = ('user', 'article')

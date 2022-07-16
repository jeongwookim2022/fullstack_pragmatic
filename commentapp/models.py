from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article

# article이 뭔지 알려주기 위해 Article을 import함

# auto_now=True
# - 언제 수정 되었는지 알 수 있음.

# article과 writer를 서버 단에서 확인해야 한다
# --> create.html에서 hidden 타입의 input을 작성함
# --> 값을 받아서 value에 넣고, 서버에 넘길 것임.
# --> 그리고 comment를 만들 때 ~~~~


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                null=True,
                                related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True,
                               related_name='comment')
    content = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now=True)
from django.db import models

###manage.py makemigrantions: models.py에 쓰는 내용을
#DB에 연동시키 위한 연결고리인 0001_initial.py를 만드는 명령어.
#이후에 0001_initial.py을 연동시키기 위한 명령어는: migrate임.
# migrate 명령어 치면, 뭔가 많이 보이는데 처음으로 이 명령어를 사용했기
# 때문에 본 pragmatic폴더, accoutapp폴더의 urls.py의 path등의 연동도 같이
# 해주는 것임.

# Create your models here.

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)

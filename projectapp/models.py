from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Project(models.Model):
    # wirter 추가. 작성자 link 추가하기 위해.
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='project', null=True)

    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
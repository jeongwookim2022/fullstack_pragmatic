
from django.contrib.auth import login
from django.forms import ModelForm
from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']    # 사용자에게 입력 받는 content를 필드에 추가

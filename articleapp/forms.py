from django.forms import ModelForm, Textarea
from django import forms

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    # 커스터마이징
    # WYSIWYG을 위해 templates에서 html 수정 필요: " | safe "
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'height: 10rem; text-align: left;'}))

    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        # Writer는 서버 내에서 설정할 것임.
        # project를 필드에 추가하여 어느 project에 article을
        # 넣을지 설정하도록 한다
        # (모델의 내용을 바꿨으므로 변경사항을 DB에 적용해야 한다)
        # --> manage.py makemigrations & migrate
        fields = ['project', 'title', 'image', 'content']


from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        # Writer는 서버 내에서 설정할 것임.
        # project를 필드에 추가하여 어느 project에 article을
        # 넣을지 설정하도록 한다
        # (모델의 내용을 바꿨으므로 변경사항을 DB에 적용해야 한다)
        # --> manage.py makemigrations & migrate
        fields = ['project', 'title', 'image', 'content']


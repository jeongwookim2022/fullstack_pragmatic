from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        # Writer는 서버 내에서 설정할 것임.
        fields = ['title', 'image', 'content']


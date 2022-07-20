from django.http import request
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from articleapp.models import Article
from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    # 여기서의 object는 comment임
    # 즉, comment의 article의 pk를 갖는 articleapp의 detail로 되돌아가도록 함.
    def get_success_url(self):
        return reverse('articleapp:detail',
                       kwargs={'pk': self.object.article.pk})

    # temp_comment.article
    # - Article중 objects에서 get하는데, pk가 request해서 받은 POST 데어터 중에서
    # - 이름이 article_pk인 pk를 가진 article을 지금 만드는 comment의 article값으로 넣어줌.
    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()

        return super().form_valid(form)


###########################################################################################


# decorator를 사용하여 request를 보내는 user가
# comment의 주인인지 아닌지 확인.
@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail',
                       kwargs={'pk': self.object.article.pk})
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView


from articleapp.models import Article
from likeapp.models import LikeRecord

# Transaction
# (1) Like에 대한 Record 생성 부분
# (2) Like 수가 올라가는 부분
# --> 위의 (1)과 (2)가 둘 다 성공해야지만 올바른 것.
#    그러므로 둘 중 하나라도 실패하면 성공한 것을 취소하도록 설정.

@transaction.atomic
def db_transaction(user, article):
    article.like += 1
    article.save()
    if LikeRecord.objects.filter(user=user, article=article).exists():
        raise ValidationError("Like already exists!")
    else:
        LikeRecord(user=user, article=article).save()

    # article.like += 1
    # article.save()



#Login한 user만 Like할 수 있도록 구현
@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']})

    def get(self, *args, **kwargs):
        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs['pk'])

        try:
            db_transaction(user, article)
            messages.add_message(self.request, messages.SUCCESS, "Successfully Liked this article!")
        except ValidationError:
            messages.add_message(self.request, messages.ERROR, "You've already Liked this article!")
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': article.pk}))

        return super(LikeArticleView, self).get(self.request, *args, **kwargs)

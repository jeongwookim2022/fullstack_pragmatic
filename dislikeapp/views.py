from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from dislikeapp.models import DisLikeRecord


@method_decorator(login_required, 'get')
class DisLikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']})

    def get(self, request, *args, **kwargs):
        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs['pk'])

        if DisLikeRecord.objects.filter(user=user, article=article).exists():
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['pk']}))
        else:
            DisLikeRecord(user=user, article=article).save()

        article.dislike += 1
        article.save()

        return super(DisLikeArticleView, self).get(self.request, *args, **kwargs)


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

#로그인이 되어있을 때 구독이 가능하므로.
from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription

@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    # project_pk를 get방식으로 받아서 그 pk를 가지고 있는
    # detail페이지로 되돌아감.
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):

        # project_pk를 가지고 있는 Project를 찾는데,
        # 만약 없으면 404 페이지를 띄움.
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user

        # 각각 요청한 user(위와 동일), project(위의 설명과 동일)인
        # subscription 정보를 찾음.
        subscription = Subscription.objects.filter(user=user,
                                                   project=project)

        # 만약 위의 구독 정보가 존재한다면,
        # 구독 취소가 됨.
        if subscription.exists():
            subscription.delete()
        # 없으면 새로 만들어서 save.
        else:
            Subscription(user=user, project=project).save()

        return super(SubscriptionView, self).get(request, *args, **kwargs)


@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 4

    # 가져 오려는 article들의 조건들을 바꿀 수 있다
    # values_list: 값들을 list화 시키는 것
    # --> models.py의 project를 list화 시킨다는 말
    # --> 구독한 모든 project들을 list로 담음.
    # 이제 field lookup을 사용하여 article list를 만듦.
    def get_queryset(self):
        project_list = Subscription.objects.filter(user=self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=project_list)

        return article_list


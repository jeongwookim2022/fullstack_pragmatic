from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article


# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
# - 게시글을 작성하려면 login이 되어 있어야 하므로

# def get_success_url(self):
# - 게시글이 작성되면 게시글에 대한 detail view로 연결

#
# - writer를 지정해줌
from commentapp.forms import CommentCreationForm


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

################################################################################

# FormMixin 클래스 상속


class ArticleDetailView(DetailView, FormMixin):
    model = Article
    # 필요성: Detial view에서는 form이 아닌 object가 있음.
    # 그런데 comment를 달 수 있는 form을 넣고 싶을 때 form이 없으므로 문제가 생긴다.
    # 이 때, FormMixin 클래스를 상속 받는다.
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'


################################################################################


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/delete.html'

    success_url = reverse_lazy('articleapp:list')


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 2


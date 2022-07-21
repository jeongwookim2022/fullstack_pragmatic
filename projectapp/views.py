from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = "projectapp/create.html"

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 4

    # 어떤 article들을 갖고 올지에 대한 필터링 같은 느낌
    # - 현재의 project와 같은 object를 가지는 project를 article을 모두 필터링하여
    #   object_list안에 넣는다
    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(project=self.get_object())

        return super(ProjectDetailView, self).get_context_data(object_list=object_list, **kwargs)


class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25


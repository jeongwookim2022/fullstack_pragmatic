from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

app_name = 'articleapp'


# TemplateView
# - 템플릿만 지정해주면 해당 템플릿을 렌더링 한다
# (rendering:유저에게 보여준다는 뜻)
urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'),
         name='list'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),

]
from django.urls import path
from django.views.generic import TemplateView

# TemplateView
# - 템플릿만 지정해주면 해당 템플릿을 렌더링 한다
# (rendering:유저에게 보여준다는 뜻)
urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'),
         name='list')
]
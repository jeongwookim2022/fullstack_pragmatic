from django.urls import path, include
from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"

urlpatterns = [
    # 1. 함수형 view는 그냥 그 함수의 이름을 그냥 적으면 된다.
    path('hello_world/', hello_world, name='hello_world'),
    # 2. 하지만, 클래스형 view에서는 views.py에 정의한 클래스를 import하고
    #  as_view()라는 메소드를 view단에 넣어줘야 한다
    path('create/', AccountCreateView.as_view(), name='create'),

]

"""pragmatic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #view에서 만든 함수 추가
    #include: APP이름/urls.py 경로의 urls.py를 참조 가능.
    # 또한 각 APP 별로 각 urls.py에서 urlpattern들을 관리할 수 있게 됨.
    # accountapp내부의 urls.py를 포함하여 그 하위 디렉토리로 분기.
    path('accounts/', include('accountapp.urls')),
    path('profiles/', include('profileapp.urls')),

]

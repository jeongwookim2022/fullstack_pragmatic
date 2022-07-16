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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #view에서 만든 함수 추가
    #include: APP이름/urls.py 경로의 urls.py를 참조 가능.
    # 또한 각 APP 별로 각 urls.py에서 urlpattern들을 관리할 수 있게 됨.
    # accountapp내부의 urls.py를 포함하여 그 하위 디렉토리로 분기.

    # static(settings)을 적음으로써 setting.py에서 STATIC에 적은 모든 값들을
    # 사용할 수 있게 됨.
    # 그 후에, MEDIA_URL과 MEDIA_ROOT를 갖고 온다.
    # --> 그러면, path들 뿐만 아니라, MEDIA_URL과 MEDIA_ROOT 또한 연결 되어지고
    # media 폴더의 내용이 수정되는 것을 확인할 수 있다.
    # --> 이렇게 해야, 이미지를 서버가 뱉어냄.
    path('accounts/', include('accountapp.urls')),
    path('profiles/', include('profileapp.urls')),
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

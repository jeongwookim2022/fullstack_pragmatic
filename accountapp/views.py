from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


        #context는 데이터 꾸러미. text라는 이름이고 내용은 POST METHOD! 이다.
        #이것('text': 'POST_METHOD')을 html에서 보낼 것임.

        #input 태그의 text 타입의 내용을, 버튼을 누르면 POST로 요청을 하며 서버에 text 타입의
        #내용을 보내는 것이므로 view의 if문에 걸리고, temp로 그 특정 'name'의 input 태그의 text 내용을
        #받고 모델의 객체를 생성하여 그 객체의 속성인 text에 temp를 저장하고 save() 메소드로 DB에 객체를 저장한다.
        # 그 후에 rendering하여 html에 temp를 보낸다.
        # 보낼 때 hello_world_output이라는 이름으로 객체를 보내고, 보낸 게 단순한 text가 아닌
        # 객체이므로, html에서는 {% %}등으로 받는다.
        # 18강: POST 요청 방식 이후
        # get 요청 방식으로 redirect 사옹하여 본 주소로 돌아가기
        # accountapp폴더의 urls.py에서 정한 app_name사용하고, urlpatterns리스트에서 path의 name으로 경로 갖고 오기
        # 이 때, reverse 함수를 사용하여 그 경로에 해당하는 경로를 다시 만든다
def hello_world(request):

    if request.user.is_authenticated:
        if request.method == "POST":

            temp = request.POST.get('hello_world_input')

            #DB에 데이터 저장
            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()

            return HttpResponseRedirect(reverse("accountapp:hello_world"))

        else:
            hello_world_list = HelloWorld.objects.all()
            return render(request, 'accountapp/hello_world.html',
                          context={'hello_world_list': hello_world_list})
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))
############################################################################################################


class AccountCreateView(CreateView):
    # 1. 모델 선택
    # 2. User 모델을 만드는 데 필요한 form
    # 3. 계정만들기에 성공했을 때, 원하는 경로로 재연결
    # reverse와의 차이는 사용되는 view의 차이. 함수형 view지, 클래스형 voew인지.
    # 4. 회원가입 중 볼 화면, 즉 html
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    #context_object_name으로 template(detail.html)에서 사용하는 user의 이름을 다르게
    #설정할 수 있다// template에서 사용할 context 변수명을 지정
    # 즉, 다른 사람의 내 페이지에 오더라도 내 정보를 볼 수 있음.
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    def get(self, *args, **kwargs):
        #로그인이 되어 있다면, 변하는 게 없는 코드
        if self.request.user.is_authenticated and \
                self.get_object() == self.request.user:
            return super().get(*args, **kwargs)

        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        #로그인이 되어 있다면, 변하는 게 없는 코드
        if self.request.user.is_authenticated and \
                self.get_object() == self.request.user:
            return super().get(*args, **kwargs)

        #Forbidden으로 금지된 곳에 접근했다고 알림
        else:
            return HttpResponseForbidden()


class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    #1. update창에서 logout하더라도, 나 포함 다른 users의 pw를
    #바꿀 수 있다는 에러가 있었음
    #2. 또한 test1로 접속해서 test1234의 계정을 지울 수 있다는 에러가
    # 있음. 이를 방지하기 위해서, self.get_object()를 통해 class에서
    # 현재 사용 중인 object(현재 user)를 갖고옴.
    # 즉, url에서 현재의 pk에 해당하는 object를 갖고 옴.
    # 그래서! 갖고 온 object가 현재(지금) requset를 보내고 있는 user와
    # 동일한지를 확인함. // self.request.user

    # --> self.get_object() == self.request.user를 통해 에러 방지.

    def get(self, *args, **kwargs):
        #로그인이 되어 있다면, 변하는 게 없는 코드
        if self.request.user.is_authenticated and \
                self.get_object() == self.request.user:
            return super().get(*args, **kwargs)

        else:
            return HttpResponseForbidden()


    def post(self, *args, **kwargs):
        #로그인이 되어 있다면, 변하는 게 없는 코드
        if self.request.user.is_authenticated and \
                self.get_object() == self.request.user:
            return super().get(*args, **kwargs)

        else:
            return HttpResponseForbidden()


class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

    #delete창에서 logout하더라도, 나 포함 다른 users의 accounts를
    #지울 수 있는 에러가 있었음

    def get(self, *args, **kwargs):
        #로그인이 되어 있다면, 변하는 게 없는 코드
        if self.request.user.is_authenticated and \
                self.get_object() == self.request.user:
            return super().get(*args, **kwargs)

        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        #로그인이 되어 있다면, 변하는 게 없는 코드
        if self.request.user.is_authenticated and \
                self.get_object() == self.request.user:
            return super().get(*args, **kwargs)

        #Forbidden으로 금지된 곳에 접근했다고 알림
        else:
            return HttpResponseForbidden()

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    # success_url = reverse_lazy('accountapp:hello_world')
    #-->
    # profile만들고 detail로 가는 게 더 자연스러움.
    # 그런데, detail은 pk를 받아야 하기 때문에, 메소드 재정의 필요.
    # def get_success_url(self)로 아래에서 재정의 한다.
    template_name = 'profileapp/create.html'

    # 서버에서 user 필드를 관리할 수 있도록 구현.
    def form_valid(self, form):
        # forms.py의 ProfileCreationForm가 보낸 데이터가 form임.
        # 그 데이터를 임시로 temp_profile 변수에 저장.
        # 즉, 실제 DB에 저장 안 하고, 임시로.
        # temp_profile에서 user필드를 request를 보낸 유저의 정보로
        # 바꾼다. 그리고 저장한다.
        # 그리고 ProfileCreateView의 원래 데이터를 return
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    #메소드 재정의
    # 설명
    # (1) self.object는 위의 model = profiled에서 profile을 가리킴.
    # 즉, profile의 user의 pk를 찾아서 넘김.
    def get_success_url(self):
        return reverse('accountapp:detail',
                       kwargs={'pk': self.object.user.pk})


#############################################################################

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    # success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail',
                       kwargs={'pk': self.object.user.pk})


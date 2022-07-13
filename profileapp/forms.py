from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        # user 필드는 서버에서 관리함.
        fields = ['image', 'nickname', 'message']


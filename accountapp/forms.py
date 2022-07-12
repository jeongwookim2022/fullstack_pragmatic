from django.contrib.auth.forms import UserCreationForm

#UserCreationForm을 상속 받아서 커스텀해서 사용할 것임.

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True
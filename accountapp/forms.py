
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm

#UserCreationForm을 상속 받아서 커스텀해서 사용할 것임.
from django.contrib.auth.password_validation import password_validators_help_text_html
from django.forms import PasswordInput


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True

        # self.fields['username'].widget = PasswordInput(attrs={"style": "margin: 0 auto; width: 35%;",
        #                                                       "class": "mt-1"})
        # self.fields['password1'].widget = PasswordInput(attrs={"style": "margin: 0 auto; width: 35%;",
        #                                                        "class": "mt-1"})

        # self.fields['password1'].help_text = "Your password can’t be too similar to your other personal information.\n" \
        #                                      "Your password must contain at least 8 characters.\n"\
        #                                      "Your password can’t be a commonly used password.\n"\
        #                                      "Your password can’t be entirely numeric."

        # self.fields['password2'].widget = PasswordInput(attrs={"style": "margin: 0 auto;; width: 35%;"})
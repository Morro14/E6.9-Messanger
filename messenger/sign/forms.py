from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from chat.views import MyUser


class BaseRegisterForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = (
            'username',
            'password',
        )




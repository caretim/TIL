from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm




class JoinForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username"]
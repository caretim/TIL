from django.contrib.auth.forms import UserCreationForm
from .models import Huser


class HuserCreateForm(UserCreationForm):
    class Meta:
        model = Huser
        fields = ["username", "email"]

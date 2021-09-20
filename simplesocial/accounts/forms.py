from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreatrForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password', 'password2')
        model = get_user_model()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Dispay Name'
        self.fields['email'].label = "Email Adddress"


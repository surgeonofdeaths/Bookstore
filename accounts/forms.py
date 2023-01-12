from django.contrib.auth import get_user_model  # looking for AUTH_USER_MODEL in settings
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        # The password field is implicitly included by default
        fields = ('email', 'username', )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', )

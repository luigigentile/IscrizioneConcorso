from django_registration.forms import RegistrationForm
from users.models import CustomUser

from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser
        fields = ('username','email','telefono')

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','email','telefono')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username','email','telefono')


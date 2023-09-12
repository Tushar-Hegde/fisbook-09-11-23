from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,UsernameField


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("reg_no",'first_name',)
        field_classes = {"reg_no":UsernameField}
        

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("reg_no",'first_name',)

from django.contrib.auth.forms import UserChangeForm


from accounts.models import CustomUser


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "birth_date", "phone_number")

from django.contrib.auth.views import PasswordResetView


from accounts.forms import CustomPasswordResetForm


class CustomPasswordReview(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'registration/password_reset_form.html'

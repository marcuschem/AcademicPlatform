from django.contrib.auth.views import LoginView


from accounts.forms import MyLoginForm


class CustomLoginView(LoginView):
    form_class = MyLoginForm
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'

from django.contrib.auth.forms import AuthenticationForm


class MyLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Usuario"
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password"].label = "Contraseña"
        self.fields["password"].widget.attrs["class"] = "form-control"
from django import forms
from django.contrib.auth.forms import UserCreationForm


from accounts.models import CustomUser


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Contraseña:",
                                widget=forms.PasswordInput(attrs={
                                    "type": "password",
                                    "name": "password",
                                    "id": "password",
                                    "placeholder": "Ingrese una contraseña.",
                                    "class": "form-control",
                                }))
    password2 = forms.CharField(label="Contraseña:",
                                widget=forms.PasswordInput(attrs={
                                    "type": "password",
                                    "name": "password",
                                    "id": "password",
                                    "placeholder": "Repita la contraseña.",
                                    "class": "form-control"
                                }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        list_fields = ["username", "first_name", "last_name", "email", "birth_date", "phone_number"]
        for element in list_fields:
            self.fields[element].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "Ingrese un nombre de usuario."
        self.fields["first_name"].widget.attrs["placeholder"] = "Ingrese su nombre."
        self.fields["last_name"].widget.attrs["placeholder"] = "Ingrese su apellido."
        self.fields["email"].widget.attrs["placeholder"] = "Ingrese su correo electrónico."
        self.fields["birth_date"].widget = forms.DateInput(attrs={"type": "date", "class": "form-control"})
        self.fields["phone_number"].widget.attrs["placeholder"] = "Ingrese su número de teléfono."

    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "birth_date", "phone_number")

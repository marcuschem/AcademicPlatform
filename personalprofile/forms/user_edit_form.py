from django import forms
from django.forms import ModelForm


from accounts.models import CustomUser


class UserEditForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name",
                  "last_name",
                  "email")
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control"
            })
        }
        labels = {
            "first_name": "Nombre",
            "last_name": "Apellido",
            "email": "Correo electrónico"
        }
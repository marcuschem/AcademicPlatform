from django import forms
from django.forms import ModelForm


from personalprofile.models import Profile


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            "about",
            "date_of_birth",
            "photo"
        )
        widgets = {
            "about": forms.Textarea(attrs={
                "class": "form-control"
            }),
            "date_of_birth": forms.DateInput(attrs={
                "class": "form-control"
            }),
            "photo": forms.FileInput(attrs={
                "class": "form-control"
            })
        }
        labels = {
            "about": "Sobre mí",
            "date_of_birth": "Fecha de nacimiento",
            "photo": "Foto de perfil"
        }

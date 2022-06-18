from django import forms
from django.contrib.auth.forms import SetPasswordForm


class CustomPasswordChangeForm(SetPasswordForm):
    new_password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su nueva contraseña.',
        'type': 'password',
        'name': 'password1'
    }))
    new_password2 = forms.CharField(label='Repita nueva contraseña', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su nueva contraseña otra vez.',
        'type': 'password',
        'name': 'password2'
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
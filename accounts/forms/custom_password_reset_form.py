from django import forms
from django.contrib.auth.forms import PasswordResetForm


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su correo.',
        'type': 'email',
        'name': 'email'
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
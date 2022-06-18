from django import forms
from django.forms import ModelForm


from lectures.models import Module


class ModuleModelForm(ModelForm):
    class Meta:
        model = Module
        fields = ('title', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }
        labels = {
            'title': 'Nombre del módulo',
            'description': 'Descripción'
        }


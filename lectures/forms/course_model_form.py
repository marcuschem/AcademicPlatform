from django import forms
from django.forms import ModelForm


from lectures.models import Course


class CourseModelForm(ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'slug', 'topic', 'overview')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'topic': forms.Select(attrs={'class': 'form-control'}),
            'overview': forms.Textarea(attrs={'class': 'form-control'})
        }
        labels = {
            'title': 'Nombre del curso',
            'slug': 'Diminutivo',
            'topic': 'Asignatura',
            'overview': 'Resumen'
        }

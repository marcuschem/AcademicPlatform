from django import forms
from django.forms import ModelForm


from practice.models import Question


class QuestionModelForm(ModelForm):

    class Meta:
        model = Question
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Título de la pregunta',
        }
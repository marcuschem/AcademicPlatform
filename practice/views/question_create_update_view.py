from django import forms
from django.apps import apps
from django.forms.models import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import TemplateResponseMixin, View


from practice.models import Contents, Question


class QuestionCreateUpdateView(TemplateResponseMixin, View):
    module = None
    model = None
    obj = None
    template_name = 'practice/manage/question/form.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.question = None

    @staticmethod
    def get_model(model_name):
        if model_name in [
            'questiontext',
            'questionimage',
            'questionfile',
            'choice',
            'answer'
        ]:
            return apps.get_model(app_label='practice', model_name=model_name)
        return None

    @staticmethod
    def get_form(model, *args, **kwargs):
        Form = modelform_factory(model,
                                 exclude=['author', 'order', 'created', 'updated'],
                                 widgets={
                                     'title': forms.TextInput(attrs={
                                         'class': 'form-control'
                                     }),
                                     'text': forms.Textarea(attrs={
                                         'class': 'form-control'
                                     }),
                                     'image': forms.FileInput(attrs={
                                         'class': 'form-control'
                                     }),
                                     'file': forms.FileInput(attrs={
                                         'class': 'form-control'
                                     }),
                                     'answer': forms.Textarea(attrs={
                                         'class': 'form-control'
                                     }),
                                     'choice': forms.Textarea(attrs={
                                         'class': 'form-control'
                                     })
                                 },
                                 labels={
                                     'title': 'Título',
                                     'text': 'Texto',
                                     'image': 'Imagen',
                                     'file': 'Archivo',
                                     'answer': 'Respuesta',
                                     'choice': 'Respuesta'
                                 })
        return Form(*args, **kwargs)

    def dispatch(self, request, question_id, model_name, id=None):
        self.question = get_object_or_404(Question, id=question_id, module__course__author=request.user)
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model, id=id, author=request.user)
        return super().dispatch(request, question_id, model_name, id)

    def get(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        if request.user.is_authenticated and request.user.is_staff:

            return self.render_to_response({'form': form,
                                            'object': self.obj})
        return HttpResponseRedirect('/login')

    def post(self, request, question_id, model_name, id=None):
        if request.user.is_authenticated and request.user.is_staff:
            form = self.get_form(self.model,
                                 instance=self.obj,
                                 data=request.POST,
                                 files=request.FILES)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.author = request.user
                obj.save()
            if not id:
                Contents.objects.create(question=self.question, question_item=obj)
                return redirect('module_question_content_list', self.question.id)
            return self.render_to_response({'form': form, 'object': self.obj})
        return HttpResponseRedirect('/login')
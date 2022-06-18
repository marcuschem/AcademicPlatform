from django import forms
from django.apps import apps
from django.forms.models import modelform_factory
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateResponseMixin, View


from lectures.models import Content, Module


class ContentCreateUpdateView(TemplateResponseMixin, View):
    module = None
    model = None
    obj = None
    template_name = 'courses/manage/content/form.html'

    @staticmethod
    def get_model(model_name):
        if model_name in ['text', 'video', 'image', 'file']:
            return apps.get_model(app_label='lectures', model_name=model_name)
        return None

    @staticmethod
    def get_form(model, *args, **kwargs):
        Form = modelform_factory(model, exclude=['author', 'order', 'created', 'updated'],
                                 widgets={
                                     'title': forms.TextInput(attrs={"class": "form-control"}),
                                     'content': forms.Textarea(attrs={"class": "form-control"}),
                                     'image': forms.FileInput(attrs={"class": "form-control"}),
                                     'video': forms.FileInput(attrs={"class": "form-control"}),
                                     'file': forms.FileInput(attrs={"class": "form-control"}),
                                 },
                                 labels={
                                     'title': 'Título',
                                     'content': 'Contenido',
                                     'image': 'Imagen',
                                     'video': 'Video',
                                     'file': 'Archivo',
                                 })
        return Form(*args, **kwargs)

    def dispatch(self, request, module_id, model_name, id=None):
        self.module = get_object_or_404(Module, id=module_id, course__author=request.user)
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model, id=id, author=request.user)
        return super().dispatch(request, module_id, model_name, id)

    def get(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        if request.user.is_authenticated and request.user.is_staff:

            return self.render_to_response({'form': form,
                                            'object': self.obj})
        return HttpResponseRedirect('/login')

    def post(self, request, module_id, model_name, id=None):
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
                Content.objects.create(module=self.module,
                                       item=obj)
                return redirect('module_content_list', self.module.course_id, self.module.id)
            return self.render_to_response({'form': form, 'object': self.obj})
        return HttpResponseRedirect('/login')

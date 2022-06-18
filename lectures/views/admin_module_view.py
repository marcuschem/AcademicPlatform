from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View


from lectures.models import Module


class AdminModuleView(View):
    template_name = 'courses/manage/module/module.html'

    @classmethod
    def get(cls, request, user_id, module_id, course_id, *args, **kwargs):
        if request.user.is_authenticated and request.user.id == user_id:
            module = Module.objects.get(id=module_id, course_id=course_id)
            return render(request, template_name=cls.template_name, context={'module': module, 'user_id': request.user.id}, *args, **kwargs)
        return HttpResponseRedirect('/login')
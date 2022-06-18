from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View


from lectures.models import Module


class ModuleContentListView(TemplateResponseMixin, View):
    template_name = 'courses/manage/content/list.html'

    def get(self, request, module_id, course_id):
        if request.user.is_authenticated and request.user.is_staff:
            module = get_object_or_404(Module, course_id=course_id, id=module_id, course__author=request.user)
            return self.render_to_response({'module': module})
        return HttpResponseRedirect('/login')
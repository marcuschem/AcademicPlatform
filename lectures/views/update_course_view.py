from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateResponseMixin, View


from lectures.forms import ModuleFormSet
from lectures.models import Course


class UpdateCourseView(TemplateResponseMixin, View):
    template_name = 'courses/manage/lecture/update.html'
    course = None

    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.course,
                             data=data)

    def dispatch(self, request, pk, *args, **kwargs):
        self.course = get_object_or_404(Course,
                                        id=pk,
                                        author=request.user, *args, **kwargs)
        return super().dispatch(request, pk, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        if request.user.is_authenticated and request.user.is_staff:
            return self.render_to_response({'course': self.course,
                                             'formset': formset})
        return HttpResponseRedirect('/login')

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)

        if formset.is_valid() and request.user.is_authenticated and request.user.is_staff:
            formset.save()
            return redirect('manage_course_list')
        return self.render_to_response({'course': self.course,
                                        'formset': formset})

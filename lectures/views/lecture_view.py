from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View


from lectures.models import Course


class LectureView(View):
    template_name = 'courses/detail.html'

    def get(self, request, user_id, course_id, *args, **kwargs):
        if request.user.is_authenticated and request.user.id == user_id:
            lecture = Course.objects.get(id=course_id)
            return render(request, template_name=self.template_name, context={'lecture': lecture, 'user_id': request.user.id}, *args, **kwargs)
        return HttpResponseRedirect('/login')

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View


from lectures.models import Module


class AdminLectureView(View):
    template_name = 'courses/manage/module/modules_list.html'

    def get(self, request, course_id, user_id, *args, **kwargs):
        paginator = Paginator(Module.objects.filter(course_id=course_id, course__author_id=user_id), 9)
        page = request.GET.get('page')
        try:
            modules = paginator.page(page)
        except PageNotAnInteger:
            modules = paginator.page(1)
        except EmptyPage:
            modules = paginator.page(paginator.num_pages)
        if request.user.is_authenticated and request.user.is_staff:
            return render(request,
                          template_name=self.template_name,
                          context={'modules': modules,
                                   'page': page,
                                   'user_id': request.user.id,
                                   'name': request.user.first_name,
                                   'course_id': course_id},
                          *args,
                          **kwargs)
        return HttpResponseRedirect('/login')
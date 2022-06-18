from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView


from lectures.models import Course


class ChangeCourseView(ListView):
    template_name = 'courses/manage/lecture/list.html'

    @classmethod
    def get(cls, request, *args, **kwargs):
        paginator = Paginator(Course.objects.filter(author=request.user.id), 9)
        page = request.GET.get('page')
        try:
            lectures = paginator.page(page)
        except PageNotAnInteger:
            lectures = paginator.page(1)
        except EmptyPage:
            lectures = paginator.page(paginator.num_pages)
        if request.user.is_authenticated and request.user.is_staff:
            return render(request,
                          template_name=cls.template_name,
                          context={'lectures': lectures,
                                   'page': page,
                                   'user': request.user,
                                   'user_id': request.user.id,
                                   'name': request.user.first_name},
                          *args,
                          **kwargs)
        return HttpResponseRedirect('/login')


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View


from lectures.models import Course


class LecturesView(View):
    template_name = 'courses/list.html'
    paginator = Paginator(Course.objects.all(), 9)

    def get(self, request, *args, **kwargs):
        page = request.GET.get('page')
        try:
            lectures = self.paginator.page(page)
        except PageNotAnInteger:
            lectures = self.paginator.page(1)
        except EmptyPage:
            lectures = self.paginator.page(self.paginator.num_pages)
        if request.user.is_authenticated:
            return render(request,
                          template_name=self.template_name,
                          context={'lectures': lectures,
                                   'page': page,
                                   'user': request.user,
                                   'user_id': request.user.id,
                                   'name': request.user.first_name},
                          *args,
                          **kwargs)
        return HttpResponseRedirect('/login')

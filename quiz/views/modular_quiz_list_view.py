from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View


from lectures.models import Module


class ModularQuizListView(View):
    template_name = 'quiz/module/list.html'

    def get(self, request, pk, *args, **kwargs):
        paginator = Paginator(Module.objects.filter(course_id=pk), 9)
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
                                   'user': request.user,
                                   'user_id': request.user.id,
                                   'name': request.user.first_name},
                          *args,
                          **kwargs)
        return HttpResponseRedirect('/login')

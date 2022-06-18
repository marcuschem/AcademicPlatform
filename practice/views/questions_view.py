from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View


from practice.models import Question


class QuestionsView(View):
    template_name = 'practice/questions_list.html'

    def get(self, request, pk, *args, **kwargs):
        paginator = Paginator(Question.objects.filter(module_id=pk), 9)
        page = request.GET.get('page')
        try:
            questions = paginator.page(page)
        except PageNotAnInteger:
            questions = paginator.page(1)
        except EmptyPage:
            questions = paginator.page(paginator.num_pages)
        if request.user.is_authenticated and request.user.is_staff:
            return render(request,
                          template_name=self.template_name,
                          context={'questions': questions,
                                   'page': page,
                                   'user': request.user,
                                   'user_id': request.user.id,
                                   'name': request.user.first_name},
                          *args,
                          **kwargs)
        return HttpResponseRedirect('/login')
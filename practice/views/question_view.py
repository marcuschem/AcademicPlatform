from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View


from practice.models import Question


class QuestionView(View):
    template_name = 'practice/content/questions.html'

    @classmethod
    def get(cls, request, user_id, question_id,  *args, **kwargs):
        if request.user.is_authenticated and request.user.id == user_id:
            question = Question.objects.get(id=question_id)
            return render(request, template_name=cls.template_name, context={'question': question, 'user_id': request.user.id}, *args, **kwargs)
        return HttpResponseRedirect('/login')
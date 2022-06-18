from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View


from practice.models import Question


class QuestionContentListView(TemplateResponseMixin, View):
    template_name = 'practice/manage/question/content.html'

    def get(self, request, question_id):
        if request.user.is_authenticated and request.user.is_staff:
            question = get_object_or_404(Question, id=question_id)
            return self.render_to_response({'question': question})
        return HttpResponseRedirect('/login')

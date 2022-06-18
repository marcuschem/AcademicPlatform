from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import  View


from practice.models import Contents


class ContentsQuestionDeleteView(View):

    def post(self, request, id):
        if request.user.is_authenticated and request.user.is_staff:
            content = get_object_or_404(Contents, id=id, question__module__course__author=request.user)
            question = content.question
            content.question_item.delete()
            content.delete()
            return redirect('module_question_content_list', question.id)
        return HttpResponseRedirect('/login')
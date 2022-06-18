from django.shortcuts import render
from django.views.generic.base import View


from quiz.models import ModularQuiz


class ScoreQuizView(View):
    template_name = 'quiz/score.html'

    def get(self, request, *args, **kwargs):
        quiz = ModularQuiz.objects.filter(student=request.user).order_by('id').latest('id')
        return render(request,
                      template_name=self.template_name,
                      context={
                          'score': quiz.score,
                          'student': request.user,
                          'user': request.user,
                          'user_id': request.user.id
                      })

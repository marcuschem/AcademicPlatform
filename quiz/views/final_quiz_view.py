from random import choices


from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy


from .modular_quiz_view import ModularQuizView
from lectures.models import Course
from practice.models import Question
from quiz.models import FinalQuiz


class FinalQuizView(ModularQuizView):
    template_name = 'quiz/final_quiz.html'
    object = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number_of_questions = 40

    @staticmethod
    def all_questions(pk):
        return list(Question.objects.filter(module__course_id=int(pk)))

    @staticmethod
    def get_parent_model(pk):
        return Course.objects.get(id=int(pk))

    @staticmethod
    def get_object(request, entity):
        return FinalQuiz.objects.create(student=request.user, course=entity)

    def generate_questions(self, request):
        pk = self.generate_pk(request)
        all_questions = self.all_questions(pk)
        entity = self.get_parent_model(pk)
        if len(all_questions) <= self.number_of_questions:
            self.object = self.get_object(request, entity)
            for question in all_questions:
                self.object.questions.add(question)
            self.object.save()
            return self.object.questions.all()
        else:
            self.object = self.get_object(request, entity)
            for question in choices(all_questions, k=self.number_of_questions):
                self.object.questions.add(question)
            self.object.save()
            return self.object.questions.all()

    def get(self, request, pk, *args, **kwargs):
        questions = list(enumerate(list(self.generate_questions(request)), start=1))
        context = {
            'pk': pk,
            'questions': questions,
            'course': self.object.course,
            'user': request.user,
            'user_id': request.user.id,
        }
        if request.user.is_authenticated:
            return render(request, template_name=self.template_name, context=context, *args, **kwargs)
        return HttpResponseRedirect('/login')

    def post(self, request, pk, *args, **kwargs):
        if request.method == "POST" and request.user.is_authenticated:
            quiz = FinalQuiz.objects.filter(student=request.user).order_by('id').latest('id')
            questions = quiz.questions.all()
            summary_dict = {
                question.title: {
                    "right": self.get_correct_answer(question),
                    "input": self.clean_student_answer(request.POST.getlist(question.title)),
                    "total": self.how_many_options(question)
                } for question in questions
            }
            checked_summary_dict = {key: self.check_question(value) for key, value in summary_dict.items()}
            quiz.score = round((self.score / (len(quiz.questions.all()) * 10)) * 100, 2)
            quiz.save(force_update=True)
            with open("log.txt", "w") as log_file:
                print(self.score, len(quiz.questions.all()), quiz.score, file=log_file, sep="\n")
            return HttpResponseRedirect(reverse_lazy('score_final_quiz_view'))
        return HttpResponseRedirect('login/')


from difflib import SequenceMatcher
from random import choices
from re import compile

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import View

from lectures.models import Module
from practice.models import Question, Answer, Choice
from quiz.models import ModularQuiz


class ModularQuizView(View):
    template_name = 'quiz/quiz.html'
    object = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.score = 0
        self.number_of_questions = 10

    @staticmethod
    def generate_pk(request):
        return request.path.replace("/", " ").split()[3]

    @staticmethod
    def all_questions(pk):
        return list(Question.objects.filter(module_id__exact=int(pk)))

    @staticmethod
    def get_parent_model(pk):
        return Module.objects.get(id=int(pk))

    @staticmethod
    def get_object(request, entity):
        return ModularQuiz.objects.create(student=request.user, module=entity)

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
            for question in choices(all_questions, k=10):
                self.object.questions.add(question)
            self.object.save()
            return self.object.questions.all()

    @staticmethod
    def get_correct_answer(question):
        list_contents = question.contents.all()
        list_answer = [content.question_item.answer for content in list_contents if
                       isinstance(content.question_item, Answer)]
        return list_answer

    @staticmethod
    def how_many_options(question):
        list_contents = question.contents.all()
        list_answer = [content.question_item.choice for content in list_contents if
                       isinstance(content.question_item, Choice)]
        return len(list_answer)

    @staticmethod
    def clean_string(answer):
        return answer.strip('\n').strip('\r')

    def clean_student_answer(self, student_answer_list):
        return list(map(self.clean_string, student_answer_list))

    def one_choice_question(self, right, input_data):
        boolean = right[0] == input_data[0]
        if boolean:
            self.score += 10
        return boolean

    def totally_string_answer(self, right, input_data):
        matcher = SequenceMatcher(None, right[0], input_data[0])
        ratio = matcher.ratio()
        boolean = ratio > 0.6
        if boolean:
            self.score += 10
        else:
            self.score += 10 * ratio
        return boolean

    def singular_numeric_answer(self, right, input_data):
        try:
            boolean = eval(right[0]) == eval(input_data[0])
        except SyntaxError:
            boolean = False
        if boolean:
            self.score += 10
        return boolean

    def complete_question(self, right, input_data):
        pattern = compile(r'([+\-]*)(\d*)\.?(\d+)((\+)+|\*{1,2}[+\-]*|(-\+)+|(\+-)+|(\+-\+)+|(-\+-)+)(\d*)\.?(\d+)')
        if pattern.match(right[0]) and pattern.match(input_data[0]):
            return self.singular_numeric_answer(right, input_data)
        return self.totally_string_answer(right, input_data)

    def check_box_question(self, right, input_data):
        question_score = 0
        good_choice_score = 10 / len(right)
        bad_choice_score = 10 / 2 * len(right)
        checker = list(zip(right, input_data))
        for answer, choice in checker:
            if answer == choice:
                question_score += good_choice_score
        if question_score > 0 and len(input_data) > len(checker):
            question_score -= (len(input_data) - len(checker)) * bad_choice_score
        if question_score > 0:
            self.score += question_score
        return question_score == 10

    def check_question(self, summary_dict):
        right = sorted(summary_dict["right"])
        input_data = sorted(summary_dict["input"])
        total = summary_dict["total"]
        if len(right) == 1 and total > 1:
            return self.one_choice_question(right, input_data)
        elif len(right) == 1 and total == 1:
            return self.complete_question(right, input_data)
        elif len(right) > 1 and total > 1:
            return self.check_box_question(right, input_data)
        else:
            self.score += 10
            with open("log.txt", "a") as log_file:
                print("A question have been inserted with mistakes", file=log_file, flush=True)
            return True

    def get(self, request, pk, *args, **kwargs):
        questions = list(enumerate(list(self.generate_questions(request)), start=1))
        context = {
            'pk': pk,
            'questions': questions,
            'module': self.object.module,
            'user': request.user,
            'user_id': request.user.id
        }
        if request.user.is_authenticated:
            return render(request, template_name=self.template_name, context=context, *args, **kwargs)
        return HttpResponseRedirect('/login')

    def post(self, request, pk, *args, **kwargs):
        if request.method == "POST" and request.user.is_authenticated:
            quiz = ModularQuiz.objects.filter(student=request.user).order_by('id').latest('id')
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
            return HttpResponseRedirect(reverse_lazy('score_quiz_view'))
        return HttpResponseRedirect('login/')

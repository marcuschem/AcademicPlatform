from django.views.generic import UpdateView
from django.urls import reverse_lazy


from practice.forms import QuestionModelForm
from practice.models import Question


class QuestionModuleView(UpdateView):
    template_name = 'practice/manage/question/create.html'
    model = Question
    form_class = QuestionModelForm

    def get_success_url(self):
        success_view_name = 'question_per_module'
        list_path = self.request.path.replace('/', " ").strip().split()
        parameters = list_path[1]
        return reverse_lazy(success_view_name, kwargs={'pk': parameters})
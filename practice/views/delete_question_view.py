from django.urls import reverse_lazy
from django.views.generic import DeleteView


from practice.models import Question


class DeleteQuestionView(DeleteView):
    template_name = 'practice/manage/question/delete.html'
    model = Question

    def get_success_url(self):
        success_view_name = 'question_per_module'
        list_path = self.request.path.replace('/', " ").strip().split()
        parameters = list_path[1]
        return reverse_lazy(success_view_name, kwargs={'pk': parameters})

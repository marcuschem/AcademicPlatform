from django.urls import reverse_lazy
from django.views.generic import DeleteView


from lectures.models import Content


class ContentDeleteView(DeleteView):
    template_name = 'courses/manage/lecture/delete.html'
    model = Content

    def get_success_url(self):
        list_parameters = self.request.path.replace("/", " ").strip().split()
        course_id = list_parameters[0]
        module_id = list_parameters[1]
        success_url = reverse_lazy('module_content_list', kwargs={
            "module_id": int(module_id),
            "course_id": int(course_id)
        })
        return success_url


from django.urls import reverse_lazy
from django.views.generic import DeleteView


from lectures.models import Module


class DeleteModuleView(DeleteView):
    template_name = 'courses/manage/lecture/delete.html'
    model = Module

    def get_success_url(self):
        list_parameters = self.request.path.replace("/", " ").strip().split()
        user_id = self.request.user.id
        course_id = list_parameters[0]
        success_url = reverse_lazy('admin_lecture_view', kwargs={
            "user_id": user_id,
            "course_id": course_id
        })
        return success_url

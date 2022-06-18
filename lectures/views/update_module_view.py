from django.views.generic import UpdateView
from django.urls import reverse_lazy


from lectures.forms import ModuleModelForm
from lectures.models import Module


class UpdateModuleView(UpdateView):
    template_name = 'courses/manage/module/create.html'
    model = Module
    form_class = ModuleModelForm

    def get_success_url(self):
        success_view_name = 'admin_lecture_view'
        list_path = self.request.path.replace('/', " ").strip().split()
        course_id = int(list_path[0])
        return reverse_lazy(success_view_name, kwargs={
            'user_id': self.request.user.id,
            'course_id': course_id
        })

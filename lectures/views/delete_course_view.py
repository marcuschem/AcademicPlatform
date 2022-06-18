from django.urls import reverse_lazy
from django.views.generic import DeleteView


from lectures.models import Course


class DeleteCourseView(DeleteView):
    template_name = 'courses/manage/lecture/delete.html'
    model = Course
    success_url = reverse_lazy('manage_course_list')
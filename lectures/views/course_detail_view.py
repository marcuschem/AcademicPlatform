from django.views.generic.detail import DetailView

from lectures.models import Course
from students.forms import CourseEnrollForm


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/lecture/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enroll_form'] = CourseEnrollForm(initial={'course': self.object})
        return context


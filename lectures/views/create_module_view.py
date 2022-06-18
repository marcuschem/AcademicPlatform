from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


from lectures.models import Module, Course
from lectures.forms import ModuleModelForm


class CreateModuleView(CreateView):
    template_name = 'practice/manage/question/create.html'
    form_class = ModuleModelForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object = None

    def get_success_url(self, **kwargs):
        return reverse_lazy('module_content_list', **kwargs)

    def form_valid(self, form):
        context = self.get_context_data()
        if form.is_valid():
            cleaned_form = form.cleaned_data
            title = cleaned_form["title"]
            course = context['course']
            self.object = Module.objects.create(title=title,
                                                  course=course)
            self.object.save()

            return HttpResponseRedirect(self.get_success_url(kwargs={
                 'course_id': course.id,
                 'module_id': self.object.id
            }))
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parameters = self.request.path.replace('/', ' ').strip().split()
        course_id = parameters[0]
        course = Course.objects.filter(id=int(course_id)).first()

        if self.request.POST and self.request.user.is_authenticated and self.request.user.is_staff:
            context['form'] = ModuleModelForm(self.request.POST)
            context['course'] = course
        else:
            context['form'] = ModuleModelForm()
            context['course'] = course
        return context
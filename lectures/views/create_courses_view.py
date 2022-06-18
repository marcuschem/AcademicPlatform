from django.http import HttpResponseRedirect
from django.views.generic import CreateView


from lectures.forms import CourseModelForm, CourseFormSet
from lectures.models import Course


class CreateCoursesView(CreateView):
    template_name = 'courses/manage/lecture/form.html'
    form_class = CourseModelForm
    model = Course

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object = None

    def get_success_url(self):
        return HttpResponseRedirect("/change")

    def form_valid(self, form):
        context = self.get_context_data()
        inlines = context['inlines']
        if inlines.is_valid() and form.is_valid():
            author = self.request.user
            cleaned_form = form.cleaned_data
            title, slug, subject, overview = cleaned_form["title"], cleaned_form["slug"], cleaned_form["topic"], \
                                             cleaned_form["overview"]
            self.object = Course.objects.create(author=author,
                                                title=title,
                                                slug=slug,
                                                topic=subject,
                                                overview=overview)
            inlines.instance = self.object
            inlines.save()
            return self.get_success_url()
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST and self.request.user.is_authenticated and self.request.user.is_staff:
            context['form'] = CourseModelForm(self.request.POST)
            context['inlines'] = CourseFormSet(self.request.POST)
        else:
            context['form'] = CourseModelForm()
            context['inlines'] = CourseFormSet()
        return context

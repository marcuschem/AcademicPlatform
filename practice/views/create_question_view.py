from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView


from lectures.models import Module
from practice.forms import QuestionModelForm
from practice.models import Question


class CreateQuestionView(CreateView):
    template_name = 'practice/manage/question/create.html'
    form_class = QuestionModelForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object = None

    def get_success_url(self, **kwargs):
        return reverse_lazy('question_per_module', **kwargs)

    def form_valid(self, form):
        context = self.get_context_data()
        if form.is_valid():
            cleaned_form = form.cleaned_data
            title = cleaned_form["title"]
            module = context['module']
            self.object = Question.objects.create(title=title,
                                                  module=module)
            self.object.save()

            return HttpResponseRedirect(self.get_success_url(kwargs={
                'pk': module.id
            }))
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parameters = self.request.path.replace('/', ' ').strip().split()
        module_id = parameters[1]
        module = Module.objects.filter(id=int(module_id)).first()

        if self.request.POST and self.request.user.is_authenticated and self.request.user.is_staff:
            context['form'] = QuestionModelForm(self.request.POST)
            context['module'] = module
        else:
            context['form'] = QuestionModelForm()
            context['module'] = module
        return context

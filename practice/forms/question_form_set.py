from django.forms.models import inlineformset_factory


from lectures.models import Module
from practice.forms import QuestionModelForm
from practice.models import Question


QuestionFormSet = inlineformset_factory(Module,
                                        Question,
                                        QuestionModelForm,
                                        fields=('title',),
                                        extra=1,
                                        can_delete=False)
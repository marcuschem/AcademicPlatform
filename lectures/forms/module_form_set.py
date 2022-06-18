from django.forms.models import inlineformset_factory


from lectures.forms import ModuleModelForm
from lectures.models import Course, Module


ModuleFormSet = inlineformset_factory(Course,
                                      Module,
                                      form=ModuleModelForm,
                                      fields=('title', 'description'),
                                      extra=1,
                                      can_delete=True
                                      )
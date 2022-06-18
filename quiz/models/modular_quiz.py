from django.db import models


from accounts.models import CustomUser
from lectures.models import Module
from practice.models import Question


class ModularQuiz(models.Model):
    module = models.ForeignKey(Module,
                               on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question,
                                       related_name="questions",
                                       blank=True)
    student = models.ForeignKey(CustomUser,
                                on_delete=models.CASCADE,
                                blank=True)
    score = models.FloatField(default=0)

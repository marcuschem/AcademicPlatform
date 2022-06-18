from django.db import models


from accounts.models import CustomUser
from lectures.models import Course
from practice.models import Question


class FinalQuiz(models.Model):
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question,
                                       related_name="final_questions",
                                       blank=True)
    student = models.ForeignKey(CustomUser,
                                on_delete=models.CASCADE,
                                blank=True)
    score = models.FloatField(default=0)
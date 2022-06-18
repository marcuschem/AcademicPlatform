from django.db import models


from practice.models import QuestionItemBase


class Answer(QuestionItemBase):
    answer = models.TextField()

    def __str__(self):
        return self.answer


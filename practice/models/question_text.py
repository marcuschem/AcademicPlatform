from django.db import models


from practice.models import QuestionItemBase


class QuestionText(QuestionItemBase):
    text = models.TextField()

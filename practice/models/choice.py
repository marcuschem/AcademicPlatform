from django.db import models


from practice.models import QuestionItemBase


class Choice(QuestionItemBase):
    choice = models.TextField()
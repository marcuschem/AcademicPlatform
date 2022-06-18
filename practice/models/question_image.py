from django.db import models


from practice.models import QuestionItemBase


class QuestionImage(QuestionItemBase):
    image = models.ImageField(upload_to='images')
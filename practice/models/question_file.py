from django.db import models


from practice.models import QuestionItemBase


class QuestionFile(QuestionItemBase):
    file = models.FileField(upload_to='files')
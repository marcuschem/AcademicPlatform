from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


from lectures.fields import OrderField
from practice.models import Question


class Contents(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='contents')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': (
        'questiontext',
        'questionimage',
        'questionfile',
        'choice',
        'answer',
    )})
    object_id = models.PositiveIntegerField()
    question_item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['question'])

    class Meta:
        ordering = ['order']
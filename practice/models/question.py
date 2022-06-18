from django.db import models
from django.utils import timezone


from lectures.fields import OrderField
from lectures.models import Module


class Question(models.Model):
    title = models.CharField(max_length=300)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    module = models.ForeignKey(Module,
                               on_delete=models.CASCADE,
                               related_name='questions')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']
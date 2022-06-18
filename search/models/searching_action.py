from django.db import models
from django.utils import timezone


from accounts.models import CustomUser


class SearchingAction(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    done = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    was_successful = models.BooleanField(default=False, blank=True)


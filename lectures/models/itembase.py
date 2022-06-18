from django.db import models


from django.template.loader import render_to_string
from accounts.models import CustomUser


class ItemBase(models.Model):
    author = models.ForeignKey(CustomUser,
                               related_name='%(class)s_related',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def render(self):
        return render_to_string(
            f'courses/content/{self._meta.model_name}.html',
            {'item': self})

    def __str__(self):
        return self.title

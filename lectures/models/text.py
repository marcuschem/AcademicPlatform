from django.db import models


from .itembase import ItemBase


class Text(ItemBase):
    content = models.TextField()


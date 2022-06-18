from django.db import models


from .itembase import ItemBase


class Video(ItemBase):
    video = models.FileField(upload_to='videos')
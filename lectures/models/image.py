from django.db import models


from .itembase import ItemBase


class Image(ItemBase):
    image = models.FileField(upload_to='images')
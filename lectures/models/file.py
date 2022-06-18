from django.db import models


from .itembase import ItemBase


class File(ItemBase):
    file = models.FileField(upload_to='files')

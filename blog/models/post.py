from django.db import models
from django.utils import timezone


from accounts.models import CustomUser
from lectures.models import Module


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               related_name="user_blog_posts")
    module = models.ForeignKey(Module,
                               on_delete=models.CASCADE,
                               related_name="module_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

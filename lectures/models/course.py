from django.db import models
from django.utils import timezone


from .subject import Subject
from accounts.models import CustomUser


class Course(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    topic = models.ForeignKey(Subject, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250,
                            null=False,
                            unique=True)
    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE)
    overview = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    students = models.ManyToManyField(CustomUser, related_name='courses_joined', blank=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

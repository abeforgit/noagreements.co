from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    'core.apps.CoreConfig'
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField('Date published', default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

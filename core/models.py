from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from noagreements import settings


class User(AbstractUser):
    email = models.EmailField(blank=False)
    profile_img = models.URLField(blank=True)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField('Date published', default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    cover_img = models.URLField(blank=True)

    def __str__(self):
        return self.title

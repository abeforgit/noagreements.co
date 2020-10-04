from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from noagreements import settings


class User(AbstractUser):
    email = models.EmailField(blank=False)
    profile_img = models.URLField(blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    show_on_home = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    pub_date = models.DateTimeField('Date published', default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cover_img = models.URLField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ["pub_date"]

    def __str__(self):
        return self.title

    def show_tags(self):
        return ", ".join(map(lambda t: str(t), self.tags.all().iterator()))

    show_tags.short_description = "tags"

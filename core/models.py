from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

from noagreements import settings


class User(AbstractUser):
    email = models.EmailField(blank=True)
    profile_img = models.URLField(blank=True)
    description = HTMLField(blank=True)
    artist_name = models.CharField(max_length=500, blank=True)

    def save(self, *args, **kwargs):
        if not self.artist_name:
            self.artist_name = self.username
        super().save(*args, **kwargs)


class ContactLink(models.Model):
    url = models.URLField(blank=True)
    name = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    show_on_home = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=500)
    content = HTMLField()
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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        TagPostPosition.objects.filter(post=self).delete()
        for tag in self.tags.all():
            newpos = TagPostPosition.objects.filter(tag=tag).last()
            if newpos is None:
                pos = 0
            else:
                pos = newpos.position + 1
            tag_post_position = TagPostPosition(post=self, tag=tag,
                                                position=pos)
            tag_post_position.save()


class TagPostPosition(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    position = models.IntegerField()

    class Meta:
        ordering = ["position"]

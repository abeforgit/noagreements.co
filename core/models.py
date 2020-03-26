from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    'core.apps.CoreConfig'
    content = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('Date published')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

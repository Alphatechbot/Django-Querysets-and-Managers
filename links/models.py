from django.db import models
from django.contrib.auth.models import User

class Link (models.Model):
    targeted_url = models.URLField
    description = models.CharField
    identifier = models.SlugField(blank=True,unique=True)
    author = models.ForeignKey(User, related_name = 'author', on_delete = models.CASCADE)
    created_date = models.DateTimeField
    active = True
    objects = models.Manager()
    public = ActiveLinkManager()


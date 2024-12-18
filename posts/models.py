""" Models for myproject """
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    """ Model for Post """
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default="fallback.png", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.title)

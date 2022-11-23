from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    time_created= models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=250)
    image =models.ImageField(null=True, blank=True, upload_to='posts')
    users_like =models.ManyToManyField(User, related_name='posts_liked', blank=True)

    class Meta:
        ordering = ['-time_created']


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    time_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-time_created']
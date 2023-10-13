from django.db import models
from django.contrib.auth.models import User

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)

class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share = models.BooleanField()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    date = models.DateField(auto_now=True)
    likes = models.ManyToManyField(Like)
    comments = models.ManyToManyField(Comment)
    shares = models.ManyToManyField(Share)

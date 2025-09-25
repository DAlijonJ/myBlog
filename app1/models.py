from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    img = models.ImageField(upload_to="new/", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)



class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comment')


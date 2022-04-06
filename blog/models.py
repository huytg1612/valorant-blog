from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from reddit.models import User

class Topic(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    background_color_code = models.CharField(max_length=20, default="#007bff")
    font_color_code = models.CharField(max_length=20, default="#ffffff")

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(range(0, 5))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ManyToManyField(Topic)

class Viewer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    viewer = models.ForeignKey(Viewer, on_delete=models.CASCADE)
    reply_to = models.ForeignKey(Viewer, on_delete=models.CASCADE, null=True, related_name="reply_to")
    tag_to = models.ManyToManyField(User)
    # content = models.TextField()
    content = RichTextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(range(0, 5), default=0)
    reply_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
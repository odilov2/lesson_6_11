from django.db import models
from django.contrib.auth.models import User
from course.models import Teacher


# Create your models here.

class BlogRole(models.Model):
    choices = None
    publish = ("p", "publish")
    draft = ("d", "draft")


class Blog(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog/blog/")
    status = models.CharField(max_length=15, choices=BlogRole.choices, default=BlogRole.publish)
    published_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.text[:15]}"



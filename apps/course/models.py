from django.db import models

# Create your models here.


class Course(models.Model):
    """
    小老师课程
    """
    owner = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField(default="")
    type = models.IntegerField(blank=True, default=0)
    score = models.IntegerField(blank=True, default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

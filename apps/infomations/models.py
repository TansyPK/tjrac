from django.db import models

# Create your models here.


class Information(models.Model):
    owner = models.IntegerField()
    question_id = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class InformationComment(models.Model):
    owner = models.IntegerField()
    information_id = models.IntegerField()
    content = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

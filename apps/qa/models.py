from django.db import models


# Create your models here.
class SelectQuestions(models.Model):
    """
    correct_code: A、B、C、D
    type: 类型
    """
    title = models.CharField(max_length=100)
    content = models.TextField(default="")
    type = models.IntegerField(blank=True, default=0)
    correct_code = models.CharField(max_length=100)
    analyzations = models.TextField(default="")
    score = models.IntegerField(blank=True, default=0)
    level = models.IntegerField(blank=True, default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class SelectAnswers(models.Model):
    """
    select_code: A、B、C、D
    type：类型
    """
    question_id = models.IntegerField()
    content = models.TextField()
    select_code = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class NormalQuestions(models.Model):
    owner = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    score = models.IntegerField(blank=True, default=0)
    type = models.IntegerField(blank=True, default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class NormalAnswers(models.Model):
    owner = models.IntegerField()
    question_id = models.IntegerField()
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class ContentQuestion(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default="")
    type = models.IntegerField(blank=True, default=0)
    analyzations = models.TextField(default="")
    score = models.IntegerField(blank=True, default=0)
    level = models.IntegerField(blank=True, default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class ContentAnswers(models.Model):
    owner = models.IntegerField()
    question_id = models.IntegerField()
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

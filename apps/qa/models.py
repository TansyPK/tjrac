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

    class Meta:
        verbose_name = "闯关选择题"
        verbose_name_plural = verbose_name


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

    class Meta:
        verbose_name = "闯关选择题回答"
        verbose_name_plural = verbose_name


class NormalQuestions(models.Model):
    owner = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    score = models.IntegerField(blank=True, default=0)
    type = models.IntegerField(blank=True, default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "讨论区问题"
        verbose_name_plural = verbose_name


class NormalAnswers(models.Model):
    owner = models.IntegerField()
    question_id = models.IntegerField()
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "讨论区回答"
        verbose_name_plural = verbose_name


class ContentQuestion(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default="")
    type = models.IntegerField(blank=True, default=0)
    analyzations = models.TextField(default="")
    score = models.IntegerField(blank=True, default=0)
    level = models.IntegerField(blank=True, default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "文本题问题"
        verbose_name_plural = verbose_name


class ContentAnswers(models.Model):
    owner = models.IntegerField()
    question_id = models.IntegerField()
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "文本题回答"
        verbose_name_plural = verbose_name


class QuestionNote(models.Model):
    owner = models.IntegerField()
    question_id = models.IntegerField()
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "选择题笔记"
        verbose_name_plural = verbose_name

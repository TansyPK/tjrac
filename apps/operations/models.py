from django.db import models


# Create your models here.
class SelectOperations(models.Model):
    question_id = models.IntegerField()
    answer_id = models.IntegerField()
    user_id = models.IntegerField()
    score = models.IntegerField(blank=True, default=0)
    is_correct = models.BooleanField(default=False)


class NormalOperations(models.Model):
    question_id = models.IntegerField()
    answer_id = models.IntegerField()
    user_id = models.IntegerField()
    score = models.IntegerField(blank=True, default=0)


class SelectTeacherOperations(models.Model):
    course_id = models.IntegerField(default=0)
    selector_id = models.IntegerField()
    teacher_id = models.IntegerField()
    room = models.IntegerField()
    status = models.IntegerField()
    interview_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class SelectCommentOperations(models.Model):
    question_id = models.IntegerField()
    owner = models.IntegerField()
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

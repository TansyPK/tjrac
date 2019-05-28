from django.db import models


# Create your models here.
class SelectOperations(models.Model):
    question_id = models.IntegerField()
    answer_id = models.IntegerField()
    user_id = models.IntegerField()
    score = models.IntegerField(blank=True, default=0)
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = "闯关记录"
        verbose_name_plural = verbose_name


class NormalOperations(models.Model):
    question_id = models.IntegerField()
    answer_id = models.IntegerField()
    user_id = models.IntegerField()
    score = models.IntegerField(blank=True, default=0)

    class Meta:
        verbose_name = "讨论区记录"
        verbose_name_plural = verbose_name


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

    class Meta:
        verbose_name = "预约操作"
        verbose_name_plural = verbose_name


class SelectCommentOperations(models.Model):
    question_id = models.IntegerField()
    owner = models.IntegerField()
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "评论操作"
        verbose_name_plural = verbose_name

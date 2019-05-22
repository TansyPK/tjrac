from django.db import models
from django.utils.timezone import now

# Create your models here.


class Course(models.Model):
    """
    小老师课程
    """
    owner = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField(default="")
    room = models.IntegerField(default=0)
    score = models.IntegerField(blank=True, default=0)
    status = models.IntegerField(default=0)  # 0 待完成 1 未完成 2 已完成
    type = models.IntegerField(default=0)
    interview_time = models.DateTimeField(default=now())
    end_time = models.DateTimeField(default=now())
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class CourseCategory(models.Model):
    """
    小老师课程类别映射表
    """
    type = models.IntegerField()
    type_name = models.CharField(max_length=100)


class CourseFeedBack(models.Model):
    """
    小老师课程反馈
    """
    order_id = models.IntegerField()
    course_id = models.IntegerField()
    selector_id = models.IntegerField()
    teacher_id = models.IntegerField()
    score = models.IntegerField()
    content = models.TextField()
    status = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

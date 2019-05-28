from django.db import models

# Create your models here.


class Information(models.Model):
    owner = models.IntegerField()
    question_id = models.IntegerField()
    content = models.CharField(max_length=100, default="test")
    score = models.IntegerField(default=0)
    type = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "邀约讲解"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class InformationComment(models.Model):
    owner = models.IntegerField()
    information_id = models.IntegerField()
    content = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "邀约讲解评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

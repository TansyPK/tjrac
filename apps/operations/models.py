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

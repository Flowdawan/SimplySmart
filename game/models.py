from django.db import models

# Create your models here.

class Question(models.Model):
    def __str__(self):
        return self.question_1
    question_1 = models.CharField(max_length=650, default='')
    answer_1_right_one = models.CharField(max_length=400, default='')
    answer_2 = models.CharField(max_length=400, default='')
    answer_3 = models.CharField(max_length=400, default='')
    answer_4 = models.CharField(max_length=400, default='')
    answer_4 = models.CharField(max_length=400, default='')

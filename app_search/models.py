from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.TextField()
    answer = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.question.split(' ')[0])
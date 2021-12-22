from django.db import models
import datetime
# Create your models here.


class Question(models.Model):
    question = models.TextField()
    answer = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.question.split(' ')[0])


class User(models.Model):
    user = models.CharField(max_length=128)
    key = models.BooleanField(default=False)
    promo_cod = models.CharField(max_length=12)

    def __str__(self):
        return self.user
from django.db import models


# Create your models here.
class Question(models.Model):
    questioner = models.CharField(max_length=40)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.questioner


class Answer(models.Model):
    answerer = models.CharField(max_length=40)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
    question_id = models.IntegerField(default=None)

    def __unicode__(self):
        return self.answerer

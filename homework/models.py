from django.db import models


# Create your models here.
class Homework(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=40)
    content = models.TextField()
    is_work = models.IntegerField(default=1)

    def __unicode__(self):
        return self.title


class Submit(models.Model):
    author = models.CharField(max_length=40)
    path = models.FileField(upload_to='./static/files', default=None)
    time = models.DateTimeField(auto_now=True)
    homework_id = models.IntegerField(default=None)
    score = models.IntegerField(default=0)

    def __unicode__(self):
        return self.author

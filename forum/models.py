from django.db import models


# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=40)
    time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Reply(models.Model):
    author = models.CharField(max_length=40)
    time = models.DateTimeField(auto_now=True)
    content = models.TextField()
    topic_id = models.IntegerField()

    def __unicode__(self):
        return self.author

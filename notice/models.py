from django.db import models


# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=40)
    content = models.TextField()

from django.db import models


# Create your models here.
class User(models.Model):
    username = models.IntegerField()
    password = models.CharField(max_length=12)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'user'

    def __unicode__(self):
        return self.username

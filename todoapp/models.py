from django.db import models
from datetime import datetime
# Create your models here.class Task(models.Model):

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
       
    def __str__(self):
        return self.title
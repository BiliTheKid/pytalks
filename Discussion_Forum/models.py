from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Topics(models.Model):
    description = models.TextField(max_length=100)
    name = models.TextField(max_length=100)
    
    def __str__(self):
        return "TOPIC : " + self.name + "  -  "+ self.description


# parent model
class forum(models.Model):
    name = models.CharField(max_length=200, default="anonymous")
    email = models.CharField(max_length=200, null=True)
    topic = models.CharField(max_length=300)
    description = models.CharField(max_length=1000, blank=True)
    link = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.topic)


# child model
class Discussion(models.Model):
    forum = models.ForeignKey(forum, blank=True, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.forum)


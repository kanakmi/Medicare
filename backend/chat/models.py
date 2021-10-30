from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

#Chat App Model

class Room(models.Model):
    name = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.TimeField(default=now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
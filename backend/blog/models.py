from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class blog(models.Model):
    by = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(default= now)
    title = models.CharField(max_length=500)
    body = models.TextField()
    likes = models.IntegerField(default=0)

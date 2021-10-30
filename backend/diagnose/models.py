from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Social Page Models

class blood_bank(models.Model):
    group = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    email = models.CharField(max_length=200)

class donations(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    disease = models.CharField(max_length=200)
    ammount = models.CharField(max_length=200)
    prescription = models.ImageField()

class request_blood(models.Model):
    hid = models.ForeignKey(blood_bank,on_delete=models.CASCADE,blank=True,null=True)
    requester = models.ForeignKey(User,on_delete=models.CASCADE)
    unit = models.IntegerField()
    prescription = models.ImageField()

class blood_donate(models.Model):
    donor = models.ForeignKey(User,on_delete=models.CASCADE)
    location = models.ForeignKey(blood_bank, on_delete=models.CASCADE)
    bgroup = models.CharField(max_length=10, default='O+')
    date = models.DateField(default=date.today())

class request_blood_public(models.Model):
    requester = models.ForeignKey(User,on_delete=models.CASCADE)
    group = models.CharField(max_length=10)
    units = models.IntegerField()
    pres = models.ImageField()



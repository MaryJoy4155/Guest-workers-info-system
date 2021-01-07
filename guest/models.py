from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class GuestWorker(models.Model):
    contact = models.CharField(max_length=200,null=True,blank=True)
    dob = models.CharField(max_length=200,null=True,blank=True)
    gender = models.CharField(max_length=200,null=True,blank=True)
    PermanantAddress = models.CharField(max_length=200,null=True,blank=True)
    TemporaryAddress = models.CharField(max_length=200,null=True,blank=True)
    District = models.CharField(max_length=200,null=True,blank=True)
    State = models.CharField(max_length=200,null=True,blank=True)
    Qualification = models.CharField(max_length=200,null=True,blank=True)
    AdharNumber = models.CharField(max_length=200,null=True,blank=True)
    IDproof = models.ImageField(max_length=200,upload_to='image/',null=True,blank=True)
    Photo = models.ImageField(max_length=200,upload_to='image/',null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)



class Contractor(models.Model):
    contact = models.CharField(max_length=200,null=True,blank=True)
    dob = models.CharField(max_length=200,null=True,blank=True)
    gender = models.CharField(max_length=200,null=True,blank=True)
    PermanantAddress = models.CharField(max_length=200,null=True,blank=True)
    TemporaryAddress = models.CharField(max_length=200,null=True,blank=True)
    District = models.CharField(max_length=200,null=True,blank=True)
    State = models.CharField(max_length=200,null=True,blank=True)
    AdharNumber = models.CharField(max_length=200,null=True,blank=True)
    IDproof = models.CharField(max_length=200,null=True,blank=True)
    Photo = models.CharField(max_length=200,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

class Sponsor(models.Model):
    contact = models.CharField(max_length=200,null=True,blank=True)
    dob = models.CharField(max_length=200,null=True,blank=True)
    gender = models.CharField(max_length=200,null=True,blank=True)
    PermanantAddress = models.CharField(max_length=200,null=True,blank=True)
    TemporaryAddress = models.CharField(max_length=200,null=True,blank=True)
    District = models.CharField(max_length=200,null=True,blank=True)
    State = models.CharField(max_length=200,null=True,blank=True)
    AdharNumber = models.CharField(max_length=200,null=True,blank=True)
    IDproof = models.CharField(max_length=200,null=True,blank=True)
    Photo = models.CharField(max_length=200,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

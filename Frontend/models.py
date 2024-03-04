from django.db import models

# Create your models here.
class ContactDb(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    subject = models.CharField(max_length=100,null=True,blank=True)
    message = models.CharField(max_length=100,null=True,blank=True)

class RegistrationDb(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)

class Cartdb(models.Model):
    username = models.CharField(max_length=20,null=True,blank=True)
    productname = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    Total = models.IntegerField(null=True,blank=True)

from django.db import models

# Create your models here.
class categorydb(models.Model):
    category = models.CharField(max_length=100,blank=True,null=True)
    description = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(upload_to="image",blank=True,null=True)

class productdb(models.Model):
    categorys = models.CharField(max_length=100,blank=True,null=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    description = models.CharField(max_length=100,blank=True,null=True)
    price = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(upload_to="image",blank=True,null=True)


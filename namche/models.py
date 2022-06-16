from email.policy import default
from pyexpat import model
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from authentication.models import CustomUser
# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    capacity=models.IntegerField()
    price=models.IntegerField()
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Team(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField()
    position=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(null=True,blank=True)


    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Food(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    category=models.CharField(max_length=100,null=True,blank=True)
    type=models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField()
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Booking(models.Model):
    uname=models.CharField('Full Name', max_length=100, null=True)
    email=models.EmailField(null=True)
    phone=models.BigIntegerField('Phone Number',null=True)
    roomname=models.ForeignKey(Room,on_delete=models.CASCADE,null=True,blank=True, default=None)
    date_from=models.DateTimeField(null=True,blank=True)
    date_to=models.DateTimeField(null=True,blank=True)
    adult=models.IntegerField(null=True,blank=True)
    message= models.TextField(max_length=1000,null=True)





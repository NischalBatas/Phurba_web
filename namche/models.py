from email.policy import default
from pyexpat import model
from unicodedata import category
from django.db import models

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



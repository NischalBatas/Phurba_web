from django import forms
from django import forms
from django.forms import ModelForm
from .models import *


class FoodForm(forms.ModelForm):
    class Meta:
        model=Food
        fields=['name','category','price','type','image' ]
        labels={
            'name': 'Enter Food Name',
            'category': 'Category',
            'price': 'Price',
            'Type': 'Type',
            'image': 'Image',
         
        }
        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
            'type': forms.TextInput(attrs={'class':'form-control'}),
        }

class RoomForm(forms.ModelForm):
    class Meta:
        model=Room
        fields=['name','capacity','price','image']
        labels={
            'name': 'Enter Room Name',
            'capacity': 'Capcity',
            'price': 'Price',
          
        }
        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'capacity': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=['uname','email','phone','roomname','date_from','date_to','adult','message']
        labels={
            'uname':'Username',
            'email':'Email',
            'phone':'Phone',
            'roomname':'Room Name',
            'date_from':'Date From',
            'date_to':'Date To',
            'adult':'Adults',
            'message':'Message'
        }
        widgets={
            'uname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'date_from':forms.DateInput(attrs={'class':'form-control'}),
            'date_to':forms.DateInput(attrs={'class':'form-control'}),
            'adult':forms.NumberInput(attrs={'class':'form-control'}),
            'message':forms.TextInput(attrs={'class':'form-control'})
        }
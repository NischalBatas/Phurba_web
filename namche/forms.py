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
